import speech_recognition as sr

class Listener:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None
    def listen(self):
        with sr.Microphone() as source:
            print("Say something!")
            self.audio = self.r.listen(source)
        with open("microphone-results.wav", "wb") as f:
            f.write(self.audio.get_wav_data())

    

