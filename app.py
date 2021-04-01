from flask import Flask
from dotenv import load_dotenv
import requests
import os
import base64
import json

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
    url = "https://api.spotify.com/v1/artists?ids=2CIMQHirSU0MQqyYHq0eOx%2C57dN52uHvrHOxijzpIgu3E%2C1vCWHaC5f2uS3yhpwWbIA6"
    response = requests.get(url, headers=hed)
    return response.json()
