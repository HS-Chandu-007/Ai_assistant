from listener import listen
from speak import speak
import features as fx

speak("Jarvis online.")

while True:
    query = listen()
    if not query:
        continue

    if "time" in query:
        speak(fx.get_current_time())
    elif "wikipedia" in query:
        speak(fx.wikipedia_summary(query))
    elif "search" in query:
        speak(fx.search_google(query))
    elif "play" in query and "youtube" in query:
        speak(fx.play_youtube_video(query))
    elif "open" in query and ("file" in query or "delete" in query):
        speak(fx.file_operation(query))
    elif "open" in query or "website" in query:
        speak(fx.open_website(query))
    elif any(app in query for app in ["chrome", "notepad", "vscode", "calculator"]):
        speak(fx.open_application(query))
    elif query.startswith("add to do"):
        task = query.replace("add to do", "").strip()
        speak(fx.todo_add(task))
    elif "show to do" in query:
        speak(fx.todo_list())
    elif "delete to do" in query:
        item = query.replace("delete to do", "").strip()
        speak(fx.todo_delete(item))
    elif "shut down" in query:
        speak(fx.shutdown_system())
        break
    elif "restart" in query:
        speak(fx.restart_system())
        break
    elif "exit" in query or "goodbye" in query:
        speak("Goodbye.")
        break
    else:
        speak(fx.gpt_fallback(query))







