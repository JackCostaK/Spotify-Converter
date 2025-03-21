# from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import yt_dlp
from youtube_search import YoutubeSearch


#For Client id and secret if using a .env file

# load_dotenv()

# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")


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
        song_name = f"{json_result["tracks"]["items"][i]["track"]["name"]} {json_result["tracks"]["items"][i]["track"]["artists"][0]["name"]}"
        song_url = get_URL(song_name)
        songs.append([song_url, song_name])

    return songs


def get_URL(title):
    

    results = YoutubeSearch(title, max_results=1).to_dict()

    url_suffix = results[0]["url_suffix"]

    url_suffix = url_suffix[:url_suffix.find("&")]

    return url_suffix


def download_song(url):

    URL = "https://www.youtube.com" + url
    print(FFMPEG_LOCATION)
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
    print(f"\nThe downloaded file name is: {filename}")



if __name__ == "__main__":

    

    #ADD FFMPEG PATH
    FFMPEG_LOCATION = ""

    URL = input("Provide Playlist URL: ")
    if FFMPEG_LOCATION == "":
        FFMPEG_LOCATION = input("Provide PATH for ffmpeg.exe: ")
    
    client_id = input("Provide client id: ")
    client_secret = input("Provide client secret: ")

    token = get_token()
    

    track_list = get_playlist_songs(token, URL )
    


    for i in range(0, len(track_list)):
        download_song(track_list[i][0])
        print(
        f"""
        
        {i+1}. {track_list[i][1]}
        PLAYLIST {int(((i+1) / (len(track_list))) * 100)}% DONE DOWNLOADING

        
        """)
