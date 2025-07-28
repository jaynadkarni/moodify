import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

# Emotion-to-music mapping with audio features
emotion_to_music_profile = {
    "joy":         {"vibe": "happy", "genre": "pop", "energy": 0.7, "danceability": 0.8, "speechiness": 0.4},
    "sadness":     {"vibe": "emotional", "genre": "acoustic", "energy": 0.3, "danceability": 0.4, "speechiness": 0.4},
    "anger":       {"vibe": "intense", "genre": "metal", "energy": 0.9, "danceability": 0.6, "speechiness": 0.4},
    "love":        {"vibe": "romantic", "genre": "r-n-b", "energy": 0.6, "danceability": 0.7, "speechiness": 0.4},
    "fear":        {"vibe": "anxious", "genre": "ambient", "energy": 0.3, "danceability": 0.3, "speechiness": 0.4},
    "surprise":    {"vibe": "wild", "genre": "edm", "energy": 0.8, "danceability": 0.8, "speechiness": 0.4},
    "grief":       {"vibe": "mourning", "genre": "piano", "energy": 0.2, "danceability": 0.2, "speechiness": 0.4},
    "excitement":  {"vibe": "hype", "genre": "electronic", "energy": 0.95, "danceability": 0.9, "speechiness": 0.4},
    "disgust":     {"vibe": "aggressive", "genre": "hard-rock", "energy": 0.85, "danceability": 0.5, "speechiness": 0.4},
    "relief":      {"vibe": "calm", "genre": "jazz", "energy": 0.4, "danceability": 0.5, "speechiness": 0.4},
}

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="12e6f0f596a74d73bdc59db773eb06d4", #st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret="6830896a1f174fddb1ac432a64a41ffa"#st.secrets["SPOTIPY_CLIENT_SECRET"]
    ))

def get_spotify_query_components(emotion):
    profile = emotion_to_music_profile.get(emotion)
    if not profile:
        return {"query": "chillhop", "filters": {}}
    query = f"{profile['vibe']} {profile['genre']}"
    filters = {
        "target_energy": profile["energy"],
        "target_danceability": profile["danceability"],
        "target_speechiness": profile["speechiness"],
        "limit": 10,
        "market": "US"
    }
    return {"query": query, "filters": filters}

def search_tracks(emotion):
    sp = get_spotify_client()
    comp = get_spotify_query_components(emotion)
    results = sp.search(q=comp["query"], type="track", limit=comp["filters"]["limit"], market="US")

    tracks = []
    for item in results["tracks"]["items"]:
        if item != None:
            name = item["name"]
            artist = item["artists"][0]["name"]
            uri = item["uri"]
            url = item["external_urls"]["spotify"]
            tracks.append((name, artist, uri, url))
    return tracks