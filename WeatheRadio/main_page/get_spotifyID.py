import spotipy
from dotenv import load_dotenv
import base64
import json
import os
from requests import post, get

load_dotenv()

cid = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
 

def get_token():
    auth_string = cid + ":" + secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_song_header():
    token = get_token()
    return {"Authorization": "Bearer " + token}

def search_for_song(song_name):
    token = get_token()
    search_url = "https://api.spotify.com/v1/search"
    headers = get_song_header()
    query = f"?q={song_name}&type=track&limit=1"

    query_url = search_url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    required_data = {"id":json_result["tracks"]["items"][0]["id"], "duration_ms": json_result["tracks"]["items"][0]["duration_ms"]}
    return required_data
