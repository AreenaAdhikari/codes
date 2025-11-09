import cv2,time,pygautai,mediapipe as mp
hands = mp.solutions.hands.Hands(max_num_hands = 1,min_detection_confidence = 0.7)
draw = mp.solutions.draw_utils
W ,H,SCROLL,DELAY = 640 , 480, 300, 1
def detect(landmarks,hands):
    fingers = [1 for t in [10,12,16,20]if landmarks.landmark[t].y<landmarks.landmark[t-2].y]
    tip,ip = landmarks.landmark[4],landmarks.landmark[3]
    if (hand=="Right" and tip.x > ip.x)(hand=="Left" and tip.x < ip.x ): fingers.append(1)
    return "scroll_up" if sum(fingers)==5 else "scroll_down" if len(fingers)==0 else "none"

cap = cv2.VideoCapture(0)
cap.set(3,W);cap.set(4,H)
print("Gesture control is Active: open palm to scrool up else fist to scroll down, press q if u want to quit")
while cap.isOpened():
    ok,img = cap.read()
    if not ok : break()
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),1)
    res = hands.process(img)
    gesture,hand = "none ", "Unknown"

    if res.multi_hand_landmarks:
        for h,info in zip(res.multi_hand_landmarks, res.multi_handedness):
            hand = info.classification[0].label
            gesture = detect(h,hand)
            draw.draw_landmarks(img,h,mp.solustions.hands.HANDS_CONNECTIONS)
        if time.time()-last>DELAY:
            pygautogui.scroll(SCROLL if gesture=="scroll_up" else -SCROLL if gesture=="scroll_down" else 0 )
            last=time.time()
    cv2.putText(img,f"Hand:{hand}| Gesture : {gesture}",(10,30),cv2.FONT_HERSHY_SIMPLEX,0.7,(255,0,0),2)
    cv2.imshow("gestur control",cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    if cv2.waitkey(1)&0xFF==ord('q'): break

cap.release() ; cv2.destroyAllWindows()