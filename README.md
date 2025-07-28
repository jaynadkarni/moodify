# Mood-Based Spotify Song Recommender

This project takes a short description of how you feel and recommends individual songs from Spotify that match your mood.

It uses:
- **Hugging Face** for emotion detection
- **Spotify Web API** for fetching songs based on vibe and audio features

---

## Features
- Detects emotions from text using Hugging Face (`SamLowe/roberta-base-go_emotions`)
- Maps detected emotions to music profiles:
  - Genre (pop, acoustic, EDM, etc.)
  - Target energy, danceability, and speechiness levels
- Fetches songs from Spotify and filters them based on their audio features
- Displays recommended songs with:
  - Track name
  - Artist name
  - Direct Spotify links

---

## How It Works
1. **User Input**: Enter how you feel (e.g., *"I feel calm but optimistic"*).
2. **Emotion Detection**: A Hugging Face model predicts the dominant emotion (like *joy*, *sadness*, *fear*).
3. **Emotion Mapping**: Each emotion is linked to a music profile (genre, vibe, energy, danceability, speechiness).
4. **Spotify Search + Filtering**:
   - Search Spotify for songs matching the vibe and genre.
   - Use Spotify audio features to filter results to fit the emotion.
5. **Output**: The app shows 5–10 recommended songs with links to play on Spotify.

---

## Requirements
- Python 3.8+
- Spotify Developer credentials (Client ID & Secret)
- Hugging Face Transformers & PyTorch (for emotion detection)
