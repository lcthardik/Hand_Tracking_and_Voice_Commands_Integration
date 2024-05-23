from voice_controller import VoiceController
from hand_tracker import HandTracker

def main():
    voice_controller = VoiceController()
    hand_tracker = HandTracker()

    while True:
        command = voice_controller.listen()
        print("You said:", command)

        if 'brakes off' in command or 'breaks off' in command:
            pyautogui.press('b')
            voice_controller.speak('Brakes released')

        elif 'follow hand' in command or 'polo hand' in command:
            voice_controller.speak('Steer using hand')
            hand_tracker.track_hand()

        elif 'exit voice' in command or 'left' in command:
            voice_controller.speak('Exiting voice commands')
            break

        else:
            voice_controller.speak('Invalid command')

if __name__ == "__main__":
    main()
