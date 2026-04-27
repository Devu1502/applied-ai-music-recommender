# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

MusicMatch 1.0

---

## 2. Intended Use

This system recommends songs based on a user’s preferred genre, mood, and energy level. It tries to find songs that are most similar to the user’s taste.


---

## 3. How It Works (Short Explanation)

The system looks at three main things: genre, mood, and energy.

Each song has these features, and the user also gives their preferred genre, mood, and energy level.

The system compares each song to the user’s preferences. If the genre matches, it adds some points. If the mood matches, it adds more points. Then it checks how close the energy level is, and gives a higher score if it is very similar.

Finally, it adds all these points together to get a total score for each song. Songs with higher scores are recommended first.


---

## 4. Data

The dataset contains about 15 songs stored in `data/songs.csv`.

I added about 5 songs to the dataset

The songs include a mix of genres like pop, rock, lofi, ambient, jazz, edm, synthwave, disco, and world. The moods include happy, chill, intense, relaxed, calm, focused, moody, peaceful, and energetic.

Overall, the dataset feels small and mostly reflects general modern music tastes, especially more popular or common styles.
---

## 5. Strengths

The recommender works well when the user has clear preferences. For example, the High-Energy Pop profile gave songs that were both energetic and matched the genre, which felt accurate.

It also works well for profiles like Chill Lofi, where the system was able to return calm and low-energy songs that match the vibe.

Another strength is that the system is simple and easy to understand. The scoring is transparent, so it is clear why each song is recommended based on genre, mood, and energy.

---

## 6. Limitations and Bias

The system is biased toward energy because energy has the biggest weight in the scoring. Because of this, songs with similar energy keep showing up even if the genre or mood does not match well.

Also, some users are not handled properly. For example, if a user chooses a mood like "sad" but there are no songs with that mood in the dataset, then the system just ignores mood completely.

Another issue is that the dataset is very small, so the same songs appear again and again. This creates a filter bubble where users don’t get much variety in recommendations.

---

## 7. Evaluation

I tested the system using different user profiles like High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicting Mood, and No Preference.

I noticed that when the preferences are clear, the results look correct. For example, High-Energy Pop gives songs that are upbeat and energetic.

One surprising thing was that some songs showed up in multiple profiles. This happens because energy has a strong influence, so songs with similar energy keep ranking high even if other features don’t match.

Also, when the user has no preference or conflicting preferences, the system mostly depends on energy, which makes the recommendations less meaningful.

---

## 8. Future Work

If I had more time, I would improve the recommender in a few ways.

First, I would add more songs to the dataset so the system can give more diverse recommendations.

Second, I would balance the scoring weights so that energy does not dominate too much and genre and mood also have a stronger impact.

Third, I would improve mood matching so similar words (like sad and moody) can still match instead of requiring exact words.

---

## 9. Personal Reflection

Building this system showed me how small changes in scoring can have a big impact on results. I was surprised that energy had such a strong effect, and that the same songs kept appearing across different profiles.

This made me realize that real music recommenders are more complex and need to balance multiple factors carefully to avoid repeating the same content.

I also learned that human judgment still really matters because the system cannot fully understand emotions or context. For example, it cannot truly understand what someone means by "sad" or "relaxing" unless it is clearly defined in the data.

---

## 10. Reflection and Ethics

### Potential Misuse

This system could be misused by over-personalizing recommendations and limiting user exposure to diverse content, creating a filter bubble. Because it relies heavily on user preferences, it may reinforce narrow listening habits instead of encouraging exploration.

To reduce this risk, future versions of the system could include diversity constraints or introduce a small level of randomness in recommendations to expose users to a wider range of music.

### AI Collaboration Reflection

AI tools were helpful in generating initial ideas for the scoring logic and structuring the recommender functions. For example, AI helped suggest how to calculate energy similarity, which improved how well songs matched user preferences.

However, some AI suggestions were overly simplistic or just did not make sense. For example, early weighting strategies did not handle trade-offs between genre and energy effectively. I had to manually adjust the weights and test different configurations to improve the system’s performance.

This showed that while AI can help with development, human judgment is still necessary to validate the system.