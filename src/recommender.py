from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(filepath):
    songs = []
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = int(row['tempo_bpm'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0
    reasons = []

    # Genre match
    if song['genre'] == user_prefs['genre']:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # Mood match
    if song['mood'] == user_prefs['mood']:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # Energy similarity
    energy_diff = abs(song['energy'] - user_prefs['energy'])
    energy_score = max(0, 1 - energy_diff)
    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    # Sort by score descending
    scored = sorted(scored, key=lambda x: x[1], reverse=True)

    return scored[:k]
