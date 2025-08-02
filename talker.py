import pyttsx3
import re

def speak(text):
    clean = re.sub(r'[^\w\s.,!?]', '', text)
    print("🧠 Jarvis:", clean)

    try:
        engine = pyttsx3.init(driverName='sapi5')  # Use Windows speech driver
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Use default voice
        engine.setProperty('rate', 180)  # Adjust speed
        engine.say(clean)
        engine.runAndWait()
    except Exception as e:
        print("❌ Error in speak():", str(e)
