import listener
import talker
import helper

talker.speak("Hello Master! I am ready to assist you.")

while True:
    print("🎙️ Listening...")
    query = listener.listen()

    if query:
        query = query.lower()
        print(f"🗣️ You said: {query}")

        if "time" in query:
            response = helper.get_current_time()
            talker.speak(response)

        elif "weather" in query:
            response = helper.get_weather()
            talker.speak(response)

        elif "exit" in query or "quit" in query:
            talker.speak("Goodbye Hermit. Shutting down.")
            break

        elif "open" in query:
            response = helper.open_website(query)
            talker.speak(response)

        elif "launch" in query or "start" in query:
            response = helper.open_application(query)
            talker.speak(response)

        elif "youtube" in query and any(word in query for word in ["play", "video", "tutorial", "music"]):
            ignore_words = ["play", "video", "videos", "on", "youtube", "tutorial", "some", "music"]
            search_terms = [word for word in query.split() if word not in ignore_words]
            cleaned_query = " ".join(search_terms).strip()

            response = helper.play_youtube_video(cleaned_query)
            talker.speak(response)

        else:
            talker.speak("Sorry, I didn’t catch that.")
    else:
        talker.speak("Sorry, I didn’t catch that.")





