import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy) 각 포인트 별 위치좌표를 알 수 있다.
                # id가 0 인 포인트에 점을 크게 그림 
                # if id == 4 :
                cv2.circle(img, (cx,cy), 15 ,(255,0,255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    # print(results.multi_hand_landmarks)



def main():

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)







if __name__ == '__main__':
    main()
