import datetime, subprocess, webbrowser, wikipedia, re, json, os, requests
from youtubesearchpython import VideosSearch
from pathlib import Path

TODO_FILE = Path("todo.json")

def get_current_time():
    return "Current time is " + datetime.datetime.now().strftime("%I:%M %p")

def wikipedia_summary(command):
    try:
        return wikipedia.summary(command.replace("wikipedia", ""), sentences=2)
    except:
        return "Couldn't find information."

def open_website(command):
    for word in command.split():
        if "." in word:
            url = word if word.startswith("http") else f"https://{word}"
            webbrowser.open(url)
            return f"Opening {url}"
    match = re.search(r"open (.+?)( website)?$", command)
    if match:
        site = match.group(1).strip().replace(" ", "")
        url = f"https://www.{site}.com"
        webbrowser.open(url)
        return f"Opening {url}"
    return search_google(command)

def search_google(command):
    query = re.sub(r"(search for|search)", "", command).strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for {query}"

def play_youtube_video(command):
    term = re.sub(r"(play|on youtube)", "", command, flags=re.IGNORECASE).strip()
    results = VideosSearch(term, limit=1).result().get("result", [])
    if results:
        video = results[0]
        webbrowser.open(video['link'])
        return f"Playing: {video['title']}"
    return "No video found."

def open_application(command):
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "vscode": r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    }
    for name, path in apps.items():
        if name in command:
            subprocess.Popen(path)
            return f"Launching {name}"
    return "App not found."

def todo_add(item):
    data = json.loads(TODO_FILE.read_text()) if TODO_FILE.exists() else []
    data.append(item)
    TODO_FILE.write_text(json.dumps(data))
    return f"Added to-do: {item}"

def todo_list():
    if not TODO_FILE.exists():
        return "To-do list is empty."
    data = json.loads(TODO_FILE.read_text())
    return "Your tasks:\n" + "\n".join([f"- {task}" for task in data])

def todo_delete(item):
    if not TODO_FILE.exists():
        return "To-do list is empty."
    data = json.loads(TODO_FILE.read_text())
    new_data = [t for t in data if item.lower() not in t.lower()]
    TODO_FILE.write_text(json.dumps(new_data))
    return f"Deleted tasks with '{item}'"

def file_operation(command):
    m = re.search(r"(open|delete) file (.+)", command)
    if m:
        action, path = m.group(1), m.group(2).strip('" ')
        if Path(path).exists():
            if action == "open":
                os.startfile(path)
                return f"Opened {path}"
            elif action == "delete":
                os.remove(path)
                return f"Deleted {path}"
    return "Invalid file command or path."

def shutdown_system():
    subprocess.run("shutdown /s /t 1", shell=True)
    return "Shutting down."

def restart_system():
    subprocess.run("shutdown /r /t 1", shell=True)
    return "Restarting."

# 🧠 Fallback using local Ollama LLaMA2
def gpt_fallback(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama2", "prompt": prompt, "stream": False}
        )
        result = response.json()
        return result.get("response", "Sorry, I couldn't generate a response.")
    except Exception as e:
        return f"Ollama error: {str(e)}"

