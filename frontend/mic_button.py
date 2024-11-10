import speech_recognition as sr

class MicButton:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def start_mic(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.recognizer.listen(source)

        try:
            print("You said: " + self.recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("Sorry, I did not understand that")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
