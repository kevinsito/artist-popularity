from flask import Flask, request
from dotenv import load_dotenv
import requests
import os
import base64
import json
import urllib

load_dotenv()
app = Flask(__name__)

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

def encode_id_secret(id, secret):
    message = id+":"+secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def get_bearer_token():
    hed = { "Authorization": "Basic "+ encode_id_secret(client_id, client_secret) }
    d = { "grant_type": "client_credentials" }
    response = requests.post("https://accounts.spotify.com/api/token", headers=hed, data=d)
    if response.status_code == 200:
        oauth_obj = response.json()
        return "Bearer " + oauth_obj['access_token']
    return null

@app.route('/')
def index():
    return ""

@app.route('/artists')
def auth():
    hed = { "Authorization": get_bearer_token() }
    args = request.args

    search = ""
    if "search" in args:
        search = urllib.parse.quote_plus(args.get("search"))
    else:
        return "Please add a search parameter!"

    search_url = ("https://api.spotify.com/v1/search?type=artist&market=AU&limit=1&query=%s" % search)
    response = requests.get(search_url, headers=hed)
    if response.status_code == 200:
        search_json = response.json()
        print (search_json)
        spotify_id = search_json['artists']['items'][0]['id']

    if spotify_id:
        tracks_url = ("https://api.spotify.com/v1/artists/%s/top-tracks?market=US&limit=2" % spotify_id)
        response = requests.get(tracks_url, headers=hed)
        if response.status_code == 200:
            top_tracks_json = response.json()
            top_tracks = {}
            for i in range(len(top_tracks_json['tracks'])):
                top_tracks[i] = top_tracks_json['tracks'][i]['name']
            return top_tracks

    return "No artist found!"
