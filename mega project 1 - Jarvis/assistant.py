import openai
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import time
import webbrowser
import subprocess
import requests
import random
import threading
import musicLibrary

# ---------------------- API KEYS ----------------------
openai.api_key = "your-openai-api-key"
newsapi = "your-newsapi-key"

# ---------------------- VOICE ENGINE ----------------------
def speak(text):
    """Speak reliably using fresh engine each time."""
    print(f"Jarvis says: {text}")
    try:
        engine = pyttsx3.init(driverName='sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # change 0/1 for male/female
        engine.setProperty('rate', 180)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as ex:
        print("Speech Error:", ex)

# ---------------------- APP PATHS ----------------------
app_paths = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "C:\\Windows\\system32\\notepad.exe",
    "spotify": "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"
}

# ---------------------- MEMORY ----------------------
chat_history = []

# ---------------------- LISTEN ----------------------
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            return recognizer.recognize_google(audio).lower()
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return None
        except sr.RequestError:
            speak("Check your internet connection.")
            return None

# ---------------------- CHAT WITH GPT ----------------------
def chat_with_ai(prompt):
    """Run GPT chat safely on thread"""
    def fetch_response():
        chat_history.append({"role": "user", "content": prompt})
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=chat_history
            )
            reply = response["choices"][0]["message"]["content"]
            chat_history.append({"role": "assistant", "content": reply})
            speak(reply)
        except Exception as e:
            speak("I am having trouble connecting to OpenAI right now.")
            print("OpenAI Error:", e)

    threading.Thread(target=fetch_response).start()

# ---------------------- OPEN APP ----------------------
def open_application(app_name):
    if app_name in app_paths:
        subprocess.Popen(app_paths[app_name])
        speak(f"Opening {app_name}.")
    else:
        speak("Application not found.")

# ---------------------- COMMAND EXECUTION ----------------------
def execute_command(command):
    words = command.lower().split(" ")

    if words[0] == "play":
        song = " ".join(words[1:])
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}.")
        else:
            speak("Song not found.")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open gpt" in command:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT.")

    elif "open" in command:
        open_application(command.replace("open", "").strip())

    elif "jarvis" in command:
        chat_with_ai(command.replace("jarvis", "").strip())

    elif "tell news" in command:
        threading.Thread(target=get_news).start()

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("I didn't understand that.")

# ---------------------- NEWS FETCH ----------------------
def get_news():
    try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])[:3]
            for article in articles:
                speak(article['title'])
        else:
            speak("Unable to fetch news right now.")
    except Exception as e:
        print("News API Error:", e)
        speak("There was a problem fetching the news.")

# ---------------------- WAKE WORD ----------------------
def wake_word_detected():
    recognizer = sr.Recognizer()
    wake_words = ["jarvis", "hey jarvis", "hi jarvis", "ok jarvis", "hello jarvis"]

    try:
        mic = sr.Microphone()
    except OSError:
        print("No microphone detected! Please check your mic settings.")
        return False

    with mic as source:
        print("Say 'Jarvis' to activate...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            word = recognizer.recognize_google(audio).lower()
            print("You said:", word)

            for wake in wake_words:
                if wake in word:
                    time.sleep(0.3)
                    speak("Yes boss")
                    return True

            return False

        except sr.UnknownValueError:
            return False

        except sr.WaitTimeoutError:
            return False

        except sr.RequestError:
            print("Could not request results, check your internet connection")
            return False

# ---------------------- MAIN ----------------------
if __name__ == "__main__":
    speak("Hello, I am Jarvis. Say 'Jarvis' to activate me.")
    while True:
        if wake_word_detected():
            command = listen()
            if command:
                execute_command(command)
