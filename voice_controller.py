import speech_recognition as sr
import pyttsx3

class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)
        return self.recognizer.recognize_google(audio).lower().strip()

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
