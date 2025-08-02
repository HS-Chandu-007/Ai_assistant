import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("🎙️ Listening...")
        audio = r.listen(src, phrase_time_limit=6)
    try:
        command = r.recognize_google(audio).lower()
        print(f"🗣 You: {command}")
        return command
    except:
        return None


