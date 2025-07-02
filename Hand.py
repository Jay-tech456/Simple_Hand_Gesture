import cv2
import mediapipe as mp

class hand:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.lmsList = []
        self.handedness = []



    def findFingers(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        thumbs_up_score = 0

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        frame, handLms, self.mpHands.HAND_CONNECTIONS
                    )

                # Convert landmark positions to pixel coordinates
                h, w, _ = frame.shape
                lm = handLms.landmark
                coords = lambda id: (int(lm[id].x * w), int(lm[id].y * h))

                # Thumb tip (4), thumb MCP (2), index tip (8), index MCP (5)
                thumb_tip = coords(4)
                thumbs_mcp = coords(2)
                index_tip = coords(8)
                index_mcp = coords(5)
                middle_tip = coords(12)
                middle_mcp = coords(9)
                ring_tip = coords(16)
                ring_mcp = coords(13)
                pinky_tip = coords(20)
                pinky_mcp = coords(17)

                conditions = [ 

                    thumb_tip[1] < thumbs_mcp[1],    # thumb is higher (y is top-down)
                    index_tip[1] > index_mcp[1],       # index finger is down
                    middle_tip[1] > middle_mcp[1],       # Middle finder is down
                    ring_tip[1] > ring_mcp[1],           # ring finder is down
                    pinky_tip[1] > pinky_mcp[1]         # pinky is down

                ]


                thumbs_up_score = sum(conditions)
                thumbs_up_percent = int((thumbs_up_score / 5) * 100)

                # Draw overlay
                cv2.putText(frame, f"Thumbs Up: {thumbs_up_percent}%", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        return frame


    def findPosition(self, frame, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmsList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmsList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                    cv2.putText(frame, f'{id}', (cx + 5, cy - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = (xmin, ymin, xmax, ymax)

            if draw:
                cv2.rectangle(frame, (xmin - 20, ymin - 20),
                              (xmax + 20, ymax + 20), (0, 255, 0), 2)

        return self.lmsList, bbox

    def getLandmarkById(self, id):
        for lm in self.lmsList:
            if lm[0] == id:
                return lm[1], lm[2]
        return None

    def __del__(self):
        self.hands.close()
