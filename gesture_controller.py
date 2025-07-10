# controller.py
import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

cap = cv2.VideoCapture(0)
wScr, hScr = pyautogui.size()
prev_x, prev_y = 0, 0
smoothening = 7
click_time = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

def fingers_up(lmList):
    tips = [4, 8, 12, 16, 20]
    fingers = []
    if lmList[tips[0]][1] > lmList[tips[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    for i in range(1, 5):
        if lmList[tips[i]][2] < lmList[tips[i] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                fingers = fingers_up(lmList)
                index_x, index_y = lmList[8][1], lmList[8][2]

                if fingers == [0, 1, 0, 0, 0]:
                    x3 = np.interp(index_x, (100, 540), (0, wScr))
                    y3 = np.interp(index_y, (100, 380), (0, hScr))
                    cur_x = prev_x + (x3 - prev_x) / smoothening
                    cur_y = prev_y + (y3 - prev_y) / smoothening
                    pyautogui.moveTo(cur_x, cur_y)
                    prev_x, prev_y = cur_x, cur_y

                if fingers == [1, 1, 0, 0, 0] and time.time() - click_time > 1:
                    pyautogui.click()
                    click_time = time.time()

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Mouse Control (Close me to stop)", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
