# Hand Gesture Mouse Control

A computer vision project that enables users to control the system mouse using hand gestures through a webcam.

This project uses **MediaPipe for hand tracking**, **OpenCV for real-time video processing**, and **PyAutoGUI for controlling mouse events**.

---

## Features

* Real-time hand tracking
* Detects **21 hand landmarks**
* Cursor movement using index finger
* Mouse click using thumb and index finger pinch gesture
* Real-time gesture detection
* Works without a physical mouse

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* Computer Vision

---

## How It Works

1. The webcam captures real-time video using OpenCV.
2. MediaPipe detects **21 hand landmarks** from the video frame.
3. The index finger controls the mouse cursor movement.
4. The distance between thumb and index finger is calculated.
5. If the distance becomes small, a mouse click event is triggered.

---

## Gesture Controls

| Gesture              | Action           |
| -------------------- | ---------------- |
| Move Index Finger    | Cursor Movement  |
| Thumb + Index Finger | Mouse Click      |
| ESC Key              | Exit Application |

---

## Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/hand-gesture-mouse-control.git
```

Move to project folder

```
cd hand-gesture-mouse-control
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Project

```
python hand_mouse.py
```

Make sure your webcam is enabled.

---

## Project Structure

```
hand-gesture-mouse-control
│
├── hand_mouse.py
├── README.md
└── requirements.txt
```

---

## Future Improvements

* Drag and drop gesture
* Scroll gesture
* Right click gesture
* Gesture smoothing
* Performance optimization

---

## Author

Sandeep Bisht
B.Tech Computer Science Engineering

GitHub: https://github.com/SandeepBisht672005
LinkedIn: https://linkedin.com/in/sandeep-bisht-268902294
