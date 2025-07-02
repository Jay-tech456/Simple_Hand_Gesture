import cv2   # To apply the computer vision 
import os
import mediapipe as mp          # An open source custom solution ML library developed by Google that allows pre-trained ML 
                                # solutions such as facial recognition, hang gestures, and much more

from Hand import hand
def open_camera():
    # 0 is usually the default camera. Change to 1 or 2 if you have multiple cameras.
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    print("Press 'q' to quit the camera feed.")

    HandDetection = hand()
    while True:
        ret, frame = cap.read()         # Reads the frame of the camera


        if not ret:
            print("Failed to grab frame")
            break

        # # Display the frame in a window named 'Camera'
        frame = HandDetection.findFingers(frame)
        lmsList,  bbox  = HandDetection.findPosition(frame)

        if len(lmsList)!=0:
            print(lmsList[0])

        # cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow('Camera', frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()
