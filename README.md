# Virtual_Mouse

**Gesture-Controlled Virtual Mouse Using Computer Vision**

Virtual_Mouse is a computer vision–based system that enables hands-free control of the mouse cursor using real-time hand gesture recognition. Built with Python, OpenCV, and MediaPipe, this application tracks hand landmarks through a webcam and translates gestures into mouse actions such as movement, clicking, dragging, and scrolling.

---

## Overview

This project uses real-time video input to detect hand landmarks and analyze finger positions. Specific gestures are mapped to mouse events, allowing users to interact with their system without physical contact with a mouse device.

---

## Key Features

* Real-time hand tracking using a standard webcam
* Cursor movement using index finger tracking
* Left-click using thumb–index finger pinch
* Right-click using thumb–pinky finger pinch
* Gesture-based drag and scroll operations
* Smooth and accurate cursor control

---

## Technology Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

---

## System Workflow

1. The webcam captures live video frames.
2. MediaPipe detects hand landmarks and finger positions.
3. Gesture logic processes the landmark coordinates.
4. PyAutoGUI executes corresponding mouse actions on the system.

---

## Installation and Execution

```bash
git clone https://github.com/thekripaverse/Virtual_Mouse.git
cd Virtual_Mouse
pip install -r requirements.txt
python virtual_mouse.py
```

Ensure that a functional webcam is connected before running the program.

---
