import speech_recognition as sr
import pyttsx3
import pyautogui
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time



r = sr.Recognizer()
def SpeakText(command):
	
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

time.sleep(3)
SpeakText('Voice command activated')

while(0):
	
	try:
		with sr.Microphone() as source2:
			r.adjust_for_ambient_noise(source2, duration=0.2)
			audio2 = r.listen(source2)
			
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			MyText=str(MyText)

			print("Did you say ",MyText)			
			if (MyText=='brakes off') or (MyText=='breaks off'):
				print("chal gya bc")
				pyautogui.press('b')
				SpeakText('breaks off')
				#break
			elif (MyText=='follow hand') or (MyText=='polo hand') :
				print("chal gya bc")
				SpeakText('steer using hand')
				cap = cv2.VideoCapture(0)
				cap.set(3, 1280)
				cap.set(4, 720)
				detector = HandDetector(detectionCon=0.8, maxHands=1)
				x,y=100,100
				pyautogui.click(x=600, y=500)
				while True:
				    _, img = cap.read()    
				    img = cv2.flip(img, 1)
				    imgRaw = img.copy()
				    hands, img = detector.findHands(img, flipType=False)
				    if hands:
				        for hand in hands:
				            x, y, w, h = hand['bbox']
				            print("x-axis: ",x," y-axis: ",y)
				            x=x+200
				            y=y+100
				        if x<0:
				            x=0
				        if x>1500:
				            x=1500
				        if y<0:
				            y=0
				        if y>500:
				            y=500
				        pyautogui.moveTo(x, y)
				    #img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))
				    cv2.imshow("Image", imgRaw)
				    if cv2.waitKey(10) == ord('q'):
				        break

			elif (MyText=='throttle up') or (MyText=='turtle up') or (MyText=='bottle up'):
				print("chal gya bc")
				SpeakText('throttle increased')
				#break
			elif (MyText=='throttle down') or (MyText=='throttle down'):
				print("chal gya bc")
				pyautogui.press('f1')
				SpeakText('throttle decreased')
				#break
			elif (MyText=='rudder right') or (MyText=='brother right'):
				print("chal gya bc")
				pyautogui.press('d')
				SpeakText('rudder moved to right')
				#break
			elif (MyText=='rudder left') or (MyText=='brother left'):
				print("chal gya bc")
				pyautogui.press('a')
				SpeakText('rudder moved to left')
				#break
			elif (MyText=='rudder center') or (MyText=='rudder centre') or (MyText=='brotherd centre') :
				print("chal gya bc")
				pyautogui.press('s')
				SpeakText('rudder moved to centre')
				#break
			elif (MyText=='exit voice') or (MyText=='left'):
				print("chal gya bc")
				SpeakText('exiting voice commands')
				break
			else:
				SpeakText('Invalid input')
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
