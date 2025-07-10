# Virtual_Mouse

# 🖱️ Virtual Mouse using Computer Vision

This project is a gesture-controlled virtual mouse built using Python, OpenCV, and MediaPipe. It enables hands-free control of your system cursor through webcam-based hand tracking.

## ✨ Features

- 📸 Real-time hand tracking via webcam
- 👆 Move cursor using index finger
- 🤏 Left-click with thumb-index pinch
- 🤙 Right-click with thumb-pinky pinch
- ✊ Gesture-based drag and scroll
- 🎯 High accuracy and smooth performance

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## 🚀 How It Works

1. Webcam detects your hand and landmarks via MediaPipe.
2. Hand gestures are interpreted using finger positions.
3. Corresponding mouse actions (move, click, drag, scroll) are performed via PyAutoGUI.

## 📦 Installation

```bash
git clone https://github.com/thekripaverse/Virtual_Mouse.git
cd Virtual_Mouse
pip install -r requirements.txt
python virtual_mouse.py
Note: Make sure your webcam is connected.

🔧 Controls
Gesture	Action
Index Finger Up	Move Mouse
Pinch (Index + Thumb)	Left Click
Pinch (Pinky + Thumb)	Right Click
Fist	Hold & Drag
2 Fingers Down	Scroll

📁 Folder Structure
cpp
Copy
Edit
Virtual_Mouse/
├── virtual_mouse.py
├── requirements.txt
├── README.md
└── assets/ (optional hand images, gesture guide)

👤 Author
Kripasree Mohanraj
GitHub | LinkedIn
