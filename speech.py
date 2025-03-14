import pyttsx3
import speech_recognition as sr

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening for command...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            return command
    except Exception as e:
        talk("Sorry, I didn't catch that.")
        return ""
