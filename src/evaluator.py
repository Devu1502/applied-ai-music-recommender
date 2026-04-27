from typing import List, Dict, Tuple
from src.recommender import recommend_songs


def evaluate_profiles(user_profiles: Dict, songs: List[Dict]) -> None:

    print("\nSystem Evaluation\n")

    for profile_name, prefs in user_profiles.items():
        recs = recommend_songs(prefs, songs, k=5)

        scores = [score for _, score, _ in recs]

        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)

        print(f"Profile: {profile_name}")
        print(f" Avg Score : {avg_score:.2f}")
        print(f" Max Score : {max_score:.2f}")
        print(f" Min Score : {min_score:.2f}")

        unique_genres = len(set(song['genre'] for song, _, _ in recs))
        print(f" Genre Diversity (top 5): {unique_genres}")

        print("-" * 40)