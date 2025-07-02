
# 🖐️ Hand Tracking & Thumbs-Up Detection with OpenCV + MediaPipe

This project uses **MediaPipe** and **OpenCV** to track a user's hand in real time via webcam. It visualizes hand landmarks, detects thumbs-up gestures, and displays the gesture confidence as a percentage on the video feed.

---

## 🚀 Features

- 🔍 Real-time hand landmark detection using MediaPipe
- 👍 Thumbs-up gesture recognition with percentage score
- 🎯 Landmark ID visualization
- 📦 Modular and extensible Python class (`Hand`) for hand tracking

---

## 📁 Project Structure

```

.
├── Hand.py          # Hand tracking class using MediaPipe
├── main.py        # Main OpenCV app that opens camera and displays hand detection
└── README.md       

````

---

## 📦 Requirements

- Python 3.7+
- OpenCV
- MediaPipe

---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/hand-thumbs-up-tracker.git
cd hand-thumbs-up-tracker
````

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install opencv-python mediapipe
```

---

## ▶️ Usage

Run the application:

```bash
python sample.py
```

You should see your webcam stream with hand landmarks drawn on your hand. If you show a thumbs-up gesture, the app will display a `"Thumbs Up: XX%"` overlay in green.

Press `q` to quit.

---

## 🧠 How It Works

* `Hand.py` initializes a MediaPipe hand model.
* `findFingers()` processes the video frame, draws landmarks, and calculates a **"thumbs up" score** by checking the relative position of each finger.
* `sample.py` opens the webcam, continuously feeds frames to the `Hand` class, and displays the result in an OpenCV window.

---

## ✍️ Customization Ideas

* 🧠 Train your own gesture recognizer on top of landmarks
* 🧪 Detect other static gestures (peace, rock, OK)
* 🔤 Integrate with sign language datasets (ASL fingerspelling)
* 💬 Use hand gestures to trigger UI events

---

## 📜 Acknowledgments

* [MediaPipe by Google](https://mediapipe.dev/)
* [OpenCV](https://opencv.org/)

---

## 👨‍💻 Author

**Manjesh Prasad**
San Francisco Bay Area
[LinkedIn](https://www.linkedin.com/in/manjesh-p-91902919a/)

```

Let me know if you want a version with badges, a demo GIF embed, or GitHub Actions integration.
```
