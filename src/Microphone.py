import speech_recognition as sr

class Microphone:
    def __init__(self):
        self.__r = sr.Recognizer()

    def listen(self) -> str:
        with sr.Microphone() as source:
            audio = self.__r.listen(source)
        response = self.__r.recognize_sphinx(audio)
        return response
