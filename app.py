from flask import Flask, request, render_template
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
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    hed = { "Authorization": get_bearer_token() }
    args = request.args
    artist = {}
    spotify_id = 0
    top_tracks = {}

    if request.method == 'POST':
        search = urllib.parse.quote_plus(request.form['search'])

        search_url = ("https://api.spotify.com/v1/search?type=artist&market=AU&limit=1&query=%s" % search)
        response = requests.get(search_url, headers=hed)
        if response.status_code == 200:
            search_json = response.json()
            print (search_json)
            artist['id'] = search_json['artists']['items'][0]['id']
            artist['name'] = search_json['artists']['items'][0]['name']
            artist['img'] = search_json['artists']['items'][0]['images'][2]

        if artist['id']:
            tracks_url = ("https://api.spotify.com/v1/artists/%s/top-tracks?market=US&limit=2" % artist['id'])
            response = requests.get(tracks_url, headers=hed)
            if response.status_code == 200:
                top_tracks_json = response.json()
                for i in range(len(top_tracks_json['tracks'])):
                    top_tracks[i] = top_tracks_json['tracks'][i]['name']

        return render_template('artist.html', artist=artist, tracks=top_tracks)

    return render_template('search.html')
    
