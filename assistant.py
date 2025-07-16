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

# Set up OpenAI API Key
openai.api_key = "your-openai-api-key"

newsapi = "Your news api"

# Initialize speech engine only once
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def set_voice(voice_index=0, rate=200):
    """Set voice and speed"""
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', rate)  
    engine.setProperty('volume', 1.0)  

set_voice(1)  # Change index based on available voices

def speak(text):
    """Safe speech execution without threading issues"""
    engine.say(text)
    engine.runAndWait()


# App Paths for opening apps
app_paths = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "C:\\Windows\\system32\\notepad.exe",
    "spotify": "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"
}

# AI Memory Storage
chat_history = []

def listen():
    """Faster speech recognition"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduced noise adjustment
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  # Reduced timeout
            return recognizer.recognize_google(audio).lower()
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return None
        except sr.RequestError:
            speak("Check your internet connection.")
            return None

def chat_with_ai(prompt):
    """Asynchronous AI response to prevent lag"""
    def fetch_response():
        chat_history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=chat_history
        )
        reply = response["choices"][0]["message"]["content"]
        chat_history.append({"role": "assistant", "content": reply})
        speak(reply)

    threading.Thread(target=fetch_response).start()

def open_application(app_name):
    """Open applications"""
    if app_name in app_paths:
        subprocess.Popen(app_paths[app_name])
        speak(f"Opening {app_name}.")
    else:
        speak("Application not found.")

def execute_command(command):
    """Process user commands"""
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
        webbrowser.open("https://chatgpt.com")
        speak("Opening ChatGPT")
    
    elif "open" in command:
        open_application(command.replace("open", "").strip())
    
    elif "jarvis" in command:
        chat_with_ai(command.replace("jarvis", "").strip())
    
    elif "tell news" in command:
        threading.Thread(target=get_news).start()
    
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("I didn't understand that.")

def get_news():
    """Fetch top 3 news headlines (faster)"""
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    if r.status_code == 200:
        articles = r.json().get('articles', [])[:3]
        for article in articles:
            speak(article['title'])

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
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Faster adjustment

        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  # Faster response
            word = recognizer.recognize_google(audio).lower()
            print("You said:", word)

            for wake in wake_words:
                if wake in word:
                    speak("Yes boss")  # Jarvis acknowledges faster
                    return True  # Activate Jarvis immediately

            return False  # No wake word detected

        except sr.UnknownValueError:
            return False  # If speech is unclear, ignore it

        except sr.WaitTimeoutError:
            return False  # If no speech detected, don't hang

        except sr.RequestError:
            print("Could not request results, check your internet connection")
            return False


if __name__ == "__main__":
    speak("Hello, I am Jarvis. Say 'Jarvis' to activate me.")
    while True:
        if wake_word_detected():
            command = listen()
            if command:
                execute_command(command)
