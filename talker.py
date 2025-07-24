import pyttsx3
import re

def speak(text):
    print(f"🧠 Assistant: {text}")
    cleaned_text = re.sub(r'[^\w\s.,!?]', '', text)

    # Create engine *inside* the function
    engine = pyttsx3.init('sapi5')  # sapi5 is for Windows
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)

    engine.say(cleaned_text)
    engine.runAndWait()
