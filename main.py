import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import time

st.set_page_config(page_title="Gesture Mouse Controller", layout="wide")
st.title("🖐️ Streamlit Gesture Mouse Controller with Instructions")

# Sidebar gesture guide
st.sidebar.header("📋 Gesture Instructions")
st.sidebar.markdown("""
- **Neutral**: All fingers down  
- **Move Cursor**: Index up  
- **Left Click**: Thumb + Index  
- **Right Click**: Thumb + Middle  
- **Double Click**: Thumb + Index + Middle  
- **Scroll**: Raise 4 fingers  
- **Drag & Drop**: Index + Middle  
- **Multi-Select**: All fingers up  
""")

start = st.checkbox("✅ Enable Gesture Control")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)
wScr, hScr = pyautogui.size()
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mpDraw = mp.solutions.drawing_utils
prev_x, prev_y = 0, 0
smoothening = 7
click_time = 0

def fingers_up(lmList):
    tips = [4, 8, 12, 16, 20]
    fingers = []
    fingers.append(1 if lmList[tips[0]][1] > lmList[tips[0] - 1][1] else 0)
    for i in range(1, 5):
        fingers.append(1 if lmList[tips[i]][2] < lmList[tips[i] - 2][2] else 0)
    return fingers

def gesture_name(fingers):
    if fingers == [0, 0, 0, 0, 0]: return "Neutral"
    elif fingers == [0, 1, 0, 0, 0]: return "Move Cursor"
    elif fingers == [1, 1, 0, 0, 0]: return "Left Click"
    elif fingers == [1, 0, 1, 0, 0]: return "Right Click"
    elif fingers == [1, 1, 1, 0, 0]: return "Double Click"
    elif fingers == [0, 1, 1, 0, 0]: return "Drag & Drop"
    elif fingers == [0, 1, 1, 1, 1]: return "Scroll"
    elif fingers == [1, 1, 1, 1, 1]: return "Multi-Select"
    else: return "Unknown"

while cap.isOpened():
    success, img = cap.read()
    if not success:
        st.warning("Camera not accessible")
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    gesture = "None"
    finger_state = ""

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                fingers = fingers_up(lmList)
                gesture = gesture_name(fingers)
                labels = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
                finger_state = " | ".join([f"{labels[i]}: {'UP' if f else 'DOWN'}" for i, f in enumerate(fingers)])
                index_x, index_y = lmList[8][1], lmList[8][2]

                # Mouse actions
                if start:
                    if gesture == "Move Cursor":
                        x3 = np.interp(index_x, (100, 540), (0, wScr))
                        y3 = np.interp(index_y, (100, 380), (0, hScr))
                        cur_x = prev_x + (x3 - prev_x) / smoothening
                        cur_y = prev_y + (y3 - prev_y) / smoothening
                        pyautogui.moveTo(cur_x, cur_y)
                        prev_x, prev_y = cur_x, cur_y
                    elif gesture == "Left Click" and time.time() - click_time > 1:
                        pyautogui.click()
                        click_time = time.time()
                    elif gesture == "Right Click" and time.time() - click_time > 1:
                        pyautogui.rightClick()
                        click_time = time.time()
                    elif gesture == "Double Click" and time.time() - click_time > 1.5:
                        pyautogui.doubleClick()
                        click_time = time.time()
                    elif gesture == "Drag & Drop":
                        pyautogui.mouseDown()
                    else:
                        pyautogui.mouseUp()
                    if gesture == "Scroll":
                        pyautogui.scroll(-30)
                    elif gesture == "Multi-Select":
                        pyautogui.keyDown("shift")
                        pyautogui.click()
                        pyautogui.keyUp("shift")

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Show overlay
    cv2.rectangle(img, (0, 0), (w, 40), (0, 0, 0), -1)
    cv2.putText(img, f"Gesture: {gesture}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(img, finger_state, (250, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

    FRAME_WINDOW.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if not start:
        pyautogui.mouseUp()
