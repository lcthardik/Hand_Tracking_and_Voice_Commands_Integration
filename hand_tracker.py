import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

class HandTracker:
    def __init__(self):
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.x, self.y = 600, 500

    def track_hand(self):
        pyautogui.click(x=self.x, y=self.y)
        while True:
            _, img = self.cap.read()
            img = cv2.flip(img, 1)
            hands, _ = self.detector.findHands(img, flipType=False)
            if hands:
                x, y, _, _ = hands[0]['bbox']
                pyautogui.moveTo(x+200, y+100)
            cv2.imshow("Hand Tracking", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
