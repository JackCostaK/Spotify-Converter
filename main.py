from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import yt_dlp
from youtube_search import YoutubeSearch




load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode("UTF-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    body = {"grant_type": "client_credentials"}

    result = post(url, headers= headers, data=body)

    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token

def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}


def get_playlist_songs(token, playlist_id):
    songs = []

    url = "https://api.spotify.com/v1/playlists/" + playlist_id
    headers = get_auth_header(token)

    result = get(url, headers=headers)

    json_result = json.loads(result.content)

    for i in range(len(json_result["tracks"]["items"])):
        song_url = get_URL(f"{json_result["tracks"]["items"][i]["track"]["name"]} {json_result["tracks"]["items"][i]["track"]["artists"][0]["name"]}")
        songs.append(song_url)

    return songs


def get_URL(title):
    

    results = YoutubeSearch(title, max_results=1).to_dict()

    return results[0]["url_suffix"]


def download_song(url):
    FFMPEG_LOCATION = "C:\\Users\\jackc\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\ffmpeg-2025-03-20-git-76f09ab647-full_build\\bin\\ffmpeg.exe"

    URL = "https://www.youtube.com" + url

    ydl_opts = {

        'ffmpeg_location':os.path.realpath(FFMPEG_LOCATION),
        'format': 'bestaudio/best',

        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(URL, download = True)

    filename = ydl.prepare_filename(info_dict)
    print(f"The downloaded file name is: {filename}")



token = get_token()

track_list = get_playlist_songs(token,"3nI5nwuS6RRFgbVKLtNbDN" )

print(len(track_list))



# for i in range(0, len(track_list)):
#     download_song(track_list[i])

