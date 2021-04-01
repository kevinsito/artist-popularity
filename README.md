# artist-popularity
This app will show an artists popularity in a graph.

<br>

## Running the Application

- Run `python3 -m venv venv`
- Then run `. venv/bin/activate`
- You can then install all project dependencies using `pip install --upgrade pip && pip install -r requirements.txt`
- Create, a .env file and fill it out with the environment variables below
- Finally run `flask run`

`.env`

```
FLASK_DEBUG=1
FLASK_ENV=development
FLASK_APP=app.py
CLIENT_ID=<your_spotify_client_id>
CLIENT_SECRET=<your_spotify_client_secret>
```