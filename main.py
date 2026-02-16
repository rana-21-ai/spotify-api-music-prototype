import os
import base64
import argparse
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

TOKEN_URL = "https://accounts.spotify.com/api/token"
SEARCH_URL = "https://api.spotify.com/v1/search"
AUDIO_FEATURES_URL = "https://api.spotify.com/v1/audio-features/"

def get_access_token(client_id, client_secret):
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {"Authorization": f"Basic {b64_auth}"}
    data = {"grant_type": "client_credentials"}

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def search_track(token, track, artist=None):
    headers = {"Authorization": f"Bearer {token}"}
    query = f"track:{track}"
    if artist:
        query += f" artist:{artist}"

    params = {"q": query, "type": "track", "limit": 1}
    response = requests.get(SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()

    items = response.json()["tracks"]["items"]
    if not items:
        raise ValueError("No track found.")
    return items[0]

def get_audio_features(token, track_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(AUDIO_FEATURES_URL + track_id, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--track", required=True)
    parser.add_argument("--artist", default=None)
    args = parser.parse_args()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise Exception("Missing Spotify credentials")

    token = get_access_token(client_id, client_secret)
    track = search_track(token, args.track, args.artist)
    features = get_audio_features(token, track["id"])

    data = {
        "track": track["name"],
        "artist": ", ".join(a["name"] for a in track["artists"]),
        "popularity": track["popularity"],
        "danceability": features["danceability"],
        "energy": features["energy"],
        "tempo": features["tempo"],
        "valence": features["valence"],
    }

    df = pd.DataFrame([data])
    df.to_csv("output.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()
