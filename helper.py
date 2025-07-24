import datetime
import webbrowser
from youtubesearchpython import VideosSearch
import os


def get_current_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."


def get_weather():
    return "Currently, weather checking is not implemented."


def open_website(site_name):
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "kaggle": "https://www.kaggle.com",
        "notion": "https://www.notion.so",
        "linkedin": "https://www.linkedin.com"
    }

    for key in websites:
        if key in site_name:
            webbrowser.open(websites[key])
            return f"Opening {key.capitalize()}."

    words = site_name.lower().split()
    for word in words:
        if "." in word:
            url = word if word.startswith("http") else f"https://{word}"
            webbrowser.open(url)
            return f"Opening {url}"

    search_url = f"https://www.google.com/search?q={site_name}"
    webbrowser.open(search_url)
    return f"I didn't recognize the site, so I'm searching for {site_name} on Google."


def open_application(app_name):
    if "notepad" in app_name:
        os.system("start notepad")
        return "Opening Notepad."

    elif "calculator" in app_name:
        os.system("start calc")
        return "Opening Calculator."

    return "Sorry, I don't recognize that application."


def play_youtube_video(query):
    try:
        print(f"🔍 Searching YouTube for: {query}")
        search = VideosSearch(query, limit=1)
        result = search.result()

        video_data = result.get("result")
        if video_data and len(video_data) > 0:
            video_url = video_data[0]["link"]
            print(f"🎬 Found video: {video_url}")
            webbrowser.open(video_url)
            return f"Playing '{video_data[0]['title']}' on YouTube."
        else:
            return "Sorry, I couldn't find any video."

    except Exception as e:
        print(f"❌ Error: {e}")
        return "Something went wrong while searching YouTube."
