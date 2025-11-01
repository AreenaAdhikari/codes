import cv2 , import numpy as np, import mediapipe as mp ,screen_control_brightness as sbc, from math import hypot
hand = mp.solutions.hands.Hands(min_detection_confidence = 0.7,min_tracking_confidence = 0.7)
draw = mp.solutions.draw_utilis
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR:Could not open web cam")
    exit()
while True:
    ok,img = cap.read()
    if not ok: break()
    img = cv2.flip(img,1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hands_landmark:
        for i,hands in enumerate(result.multi_hands_landmark):
            label = result.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img,hand,mp.solutions.hands.HAND_CONNECTIONS)
            thumb = hand.landmark(mp.solutions.hands.hand_THUMB_TIP)
            index = hand.landmark(mp.solutions.hands.hand_INDEX_FINGER_TIP)
            h,w,_= 