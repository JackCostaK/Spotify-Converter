from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

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
        songs.append(f"{json_result["tracks"]["items"][i]["track"]["name"]} {json_result["tracks"]["items"][i]["track"]["artists"][0]["name"]}")

    return songs



token = get_token()

get_playlist_songs(token,"3nI5nwuS6RRFgbVKLtNbDN" )

