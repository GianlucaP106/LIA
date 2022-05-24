"""
An audio interpreter for testing purposes and a speech to text converter

"""
import json
import speech_recognition as sr

class Interpreter:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None

    def listen(self, path):
        """listens with computer microphone for testing puposes (ensure to install requirements)"""
        with sr.Microphone() as source:
            print("Say something!")
            self.audio = self.r.listen(source)
        with open(path, "wb") as f:
            f.write(self.audio.get_wav_data())
            
    def convertToText(self, path):
        """takes in a path to audio files and returns interpreted text"""
        with sr.AudioFile(path) as source:
            audioData = self.r.record(source)
            text = self.r.recognize_google(audioData)
            return text

