import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)


cap = cv2.VideoCapture(0)


finger_tips = [8, 12, 16, 20]  
thumb_tip = 4
thumb_ip = 3  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    total_fingers = 0  

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_no, (hand_landmarks, hand_handedness) in enumerate(
            zip(result.multi_hand_landmarks, result.multi_handedness), start=1
        ):
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            fingers = 0
            hand_label = hand_handedness.classification[0].label  

            
            if hand_label == "Right":
                if lm_list[thumb_tip][0] < lm_list[thumb_ip][0]:
                    fingers += 1
            else:  
                if lm_list[thumb_tip][0] > lm_list[thumb_ip][0]:
                    fingers += 1

            
            for tip in finger_tips:
                if lm_list[tip][1] < lm_list[tip - 2][1]:
                    fingers += 1

            total_fingers += fingers  

            
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            x, y = lm_list[9]
            cv2.putText(frame, f"{hand_label}: {fingers}", (x - 50, y - 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    
    cv2.putText(frame, f"Total Fingers: {total_fingers}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

    cv2.imshow("Finger Counter (Both Hands + Total)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
