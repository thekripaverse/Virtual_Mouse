import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
from utils.clipboard_utils import copy_text, paste_text

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    print("Proton:", text)
    engine.say(text)
    engine.runAndWait()

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            return ""

def start_proton():
    speak("Hello, I am Proton. Ready to assist you.")

    while True:
        command = get_command()
        if 'search' in command:
            speak("What should I search?")
            query = get_command()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the results for {query}.")

        elif 'map' in command or 'location' in command:
            speak("Which location?")
            loc = get_command()
            webbrowser.open(f"https://www.google.com/maps/place/{loc}")
            speak(f"Showing {loc} on Google Maps.")

        elif 'time' in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {now}.")

        elif 'copy' in command:
            copy_text()
            speak("Copied.")

        elif 'paste' in command:
            paste_text()
            speak("Pasted.")

        elif 'open file' in command:
            os.system("explorer")
            speak("Opened File Explorer.")

        elif 'sleep' in command:
            speak("Going to sleep mode.")
            break

        elif 'exit' in command or 'bye' in command:
            speak("Goodbye. Shutting down.")
            exit()
