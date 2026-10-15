# A small hardcoded database of songs
MUSIC_DATABASE = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Synthwave", "mood": "Happy"},
    {"title": "Save Your Tears", "artist": "The Weeknd", "genre": "Synthwave", "mood": "Sad"},
    {"title": "Get Lucky", "artist": "Daft Punk", "genre": "Disco", "mood": "Groovy"},
    {"title": "Instant Crush", "artist": "Daft Punk", "genre": "Synthwave", "mood": "Cool"},
    {"title": "Levitating", "artist": "Dua Lipa", "genre": "Pop", "mood": "Happy"},
    {"title": "Don't Start Now", "artist": "Dua Lipa", "genre": "Pop", "mood": "Happy"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "mood": "Emo"},
    {"title": "Starlight", "artist": "Muse", "genre": "Rock", "mood": "Sad"},
]


def recommend_music(preference):
  """Recommends songs based on a matching genre or artist or mood (case-insensitive)."""
  preference = preference.strip().lower()
  matches = []

  for song in MUSIC_DATABASE:
    # Check if preference matches genre or artist
    if (
        preference == song["genre"].lower()
        or preference == song["artist"].lower()
        or preference == song ["mood"]./lower()
    ):
      matches.append(song)

  return matches


def main():
  print("=== Simple Python Music Recommender ===")
  print("Available genres: Synthwave, Disco, Pop, Rock")
  print("Available artists: The Weeknd, Daft Punk, Dua Lipa, Ed Sheeran, Muse\n")
  print("Available artists: Happy, Sad, Groovy, Cool, Emo")

  while True:
    user_input = input(
        "Enter a favorite genre or artist or mood(or type 'quit' to exit): "
    )
    if user_input.lower() == "quit":
      print("Goodbye!")
      break

    recommendations = recommend_music(user_input)

    if recommendations:
      print("\nWe think you might like these songs:")
      for song in recommendations:
        print(f" - '{song['title']}' by {song['artist']} [{song['genre']}] [{song['mood']}")
      print()
    else:
      print(
          "\nSorry, we found no matches for that preference. Try another"
          " genre or artist.\n"
      )


if __name__ == "__main__":
  main()
