# Spotify API Music Prototype 🎧

A small Python prototype exploring music metadata and audio features using the Spotify Web API.

## Overview
This project demonstrates how Spotify’s API can be used to retrieve track-level metadata and audio features such as:
Danceability
Energy
Tempo
Valence
Popularity

The goal is to explore how these features can support music understanding, personalization, and recommendation workflows.

## What This Project Does
Authenticates using Spotify Client Credentials Flow
Searches for a track by name (and optional artist)
Retrieves detailed audio features
Outputs the results in a structured format (CSV + console output)

## Technologies Used
- Python
- Spotify Web API
- Requests
- Pandas
- dotenv

## Example Usage
```bash
python main.py --track "Blinding Lights" --artist "The Weeknd"

Output

The script prints the track’s audio features and saves them to output.csv.


Why This Matters

Audio features like energy, tempo, and valence are core signals used in:

Music recommendation systems
Mood-based playlists
Personalization and discovery experiences


This prototype reflects an early-stage exploration of data-driven music intelligence.
## Setup
1. Create a Spotify Developer account and register an app.
2. Create a `.env` file with:
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   python main.py --track "Blinding Lights" --artist "The Weeknd"

