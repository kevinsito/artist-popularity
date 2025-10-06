from flask import Flask, request, render_template
from dotenv import load_dotenv
from models import Artist, Track
import requests
import os
import base64
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
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    hed = { "Authorization": get_bearer_token() }
    artist = {}
    top_tracks = {}

    if request.method == 'POST':
        search = urllib.parse.quote_plus(request.form['search'])

        search_url = ("https://api.spotify.com/v1/search?type=artist&market=US&limit=1&query=%s" % search)
        response = requests.get(search_url, headers=hed)
        if response.status_code == 200:
            search_json = response.json()
            print (search_json)
            artist_obj = Artist(
                id=search_json['artists']['items'][0]['id'],
                name=search_json['artists']['items'][0]['name'],
                img=search_json['artists']['items'][0]['images'][0],
                followers=search_json['artists']['items'][0]['followers']['total'],
                popularity=search_json['artists']['items'][0]['popularity']
            )
            artist = artist_obj.to_dict()

        if artist['id']:
            tracks_url = ("https://api.spotify.com/v1/artists/%s/top-tracks?market=US&limit=2" % artist['id'])
            response = requests.get(tracks_url, headers=hed)
            if response.status_code == 200:
                top_tracks_json = response.json()
                print (top_tracks_json)
                for track in top_tracks_json['tracks']:
                    track_obj = Track(
                        name=track['name'],
                        album=track['album']['name'],
                        popularity=track['popularity'],
                        release_date=track['album']['release_date'],
                        img=track['album']['images'][0]
                    )
                    top_tracks[track['name']] = track_obj.to_dict()

        return render_template('artist.html', artist=artist, tracks=top_tracks)

    return render_template('search.html')
    
