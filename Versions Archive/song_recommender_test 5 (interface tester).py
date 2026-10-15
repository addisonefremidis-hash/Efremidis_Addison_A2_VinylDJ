import tkinter as tk

# Creating the interface
root = tk.Tk()
root.title("Vinyl DJ")
root.geometry("400x300")
root.mainloop()

import random  # <-- 1. Added at the top to select a single song

# A hardcoded database of records (Fixed missing spaces inside merged strings)
MUSIC_DATABASE = [
    {"title": "Channel Orange", "artist": "Frank Ocean", "genres": "RnB", "moods": "Chill"},
    {"title": "Atavista", "artist": "Childish Gambino", "genres": "Rap RnB", "moods": "Sad"},
    {"title": "Because The Internet", "artist": "Childish Gambino", "genres": "Rap", "moods": "Bold"},
    {"title": "Chromakopia", "artist": "Tyler The Creator", "genres": "Rap Alternative", "moods": "Bold"},
    {"title": "Igor ", "artist": "Tyler The Creator", "genres": "Rap Alternative", "moods": "Lonely"},
    {"title": "808s and Heartbreak", "artist": "Kanye West", "genres": "Rap", "moods": "Lonely"},
    {"title": "Late Registration", "artist": "Kanye West", "genres": "Rap", "moods": "Cool"},
    {"title": "The College Dropout", "artist": "Kanye West", "genres": "Rap", "moods": "Bold"},
    {"title": "The Anthology", "artist": "A Tribe Called Quest", "genres": "Rap RnB", "moods": "Cool Chill"},
    {"title": "Dawn FM", "artist": "The Weeknd", "genres": "Rap Alternative", "moods": "Bold"},
    {"title": "Epiphany: The Best of Chaka Khan Vol 1", "artist": "Chaka Khan", "genres": "Disco Soul", "moods": "Groovy"},
    {"title": "Cest Chic", "artist": "Chic", "genres": "Disco Dance", "moods": "Happy"},
    {"title": "The Miseducation of Ms. Lauryn Hill", "artist": "Lauryn Hill", "genres": "RnB Rap", "moods": "Chill"},
    {"title": "Bad", "artist": "Michael Jackson", "genres": "Dance Pop", "moods": "Cool Bold"},
    {"title": "Thriller", "artist": "Michael Jackson", "genres": "Pop Dance", "moods": "Groovy"},
    {"title": "Off The Wall", "artist": "Michael Jackson", "genres": "Disco Dance", "moods": "Energy"},
    {"title": "Cry", "artist": "Cigarettes After Sex", "genres": "Alternative", "moods": "Lonely Chill"},
    {"title": "SOS Deluxe: Lana", "artist": "SZA", "genres": "RnB", "moods": "Chill"},
    {"title": "Make it Big", "artist": "Wham", "genres": "Pop Dance", "moods": "Happy"},
    {"title": "The Edge of heaven", "artist": "Wham", "genres": "Pop Dance", "moods": "Energy"},
    {"title": "Arrival", "artist": "Abba", "genres": "Disco Pop", "moods": "Groovy"},
    {"title": "I Wanna Dance With Somebody", "artist": "Whitney Houston", "genres": "Disco Dance Pop", "moods": "Happy"},
    {"title": "Consience", "artist": "Womack&Womack", "genres": "RnB Funk", "moods": "Chill Happy"},
    {"title": "Collection", "artist": "Diana Ross", "genres": "Disco Soul", "moods": "Groovy"},
    {"title": "Break Out", "artist": "Pointer Sisters", "genres": "Disco Dance", "moods": "Groovy Energy"},
    {"title": "Give me the Night", "artist": "George Benson", "genres": "Soul Funk", "moods": "Cool Groovy"},
    {"title": "Give me the Reason", "artist": "Luther Vandross", "genres": "Soul Funk", "moods": "Happy Groovy"},
    {"title": "Innocent Man", "artist": "Billy Joel", "genres": "Rock", "moods": "Bold"},
    {"title": "Right Back Where we Started from", "artist": "Sinatta", "genres": "Pop", "moods": "Happy"},
    {"title": "Funky Town", "artist": "Pseudo Echo", "genres": "Pop Alternative", "moods": "Happy Energy"},
    {"title": "Hot Stuff", "artist": "Donna Summer", "genres": "Disco Dance", "moods": "Groovy"},
    {"title": "Tradgedy", "artist": "Bee Gees", "genres": "Rock Disco", "moods": "Energy"},
    {"title": "Step By Step", "artist": "New Kidz on The Block", "genres": "Pop", "moods": "Energy"},
    {"title": "Rapper's Delight", "artist": "The Sugar Hill Gang", "genres": "Rap Dance Funk", "moods": "Groovy Energy"},
    {"title": "Love is a Battlefield", "artist": "Pat Benetar", "genres": "Pop", "moods": "Bold"},
    {"title": "Step Back in Time", "artist": "Kylie Minogue", "genres": "Pop", "moods": "Happy Energy"},
    {"title": "Stonelove", "artist": "Kool & The Gang", "genres": "Funk RnB", "moods": "Happy"},
    {"title": "tell it to my Heart", "artist": "Taylor Dayne", "genres": "Pop", "moods": "Happy"},
    {"title": "Footloose", "artist": "Mixed Artists", "genres": "Dance Pop", "moods": "Groovy"},
    {"title": "Saturday Night Fever", "artist": "Mixed Artists", "genres": "Disco Dance", "moods": "Groovy"},
    {"title": "Sensational 70's", "artist": "Mixed Artists", "genres": "Soul Funk", "moods": "Groovy"},
]

def recommend_music(preference):
    """Gathers all partial matching records and returns exactly ONE random song."""
    preference = preference.strip().lower()
    matches = []

    for song in MUSIC_DATABASE:
        # 2. Fixed: Using 'in' instead of '==' allows matching single tags inside combined strings
        if preference in song["genres"].lower() or preference in song["moods"].lower():
            matches.append(song)

    # 3. If matching songs exist, pick one at random. Otherwise, return None.
    if matches:
        return random.choice(matches)
    return None

def main():
    print("=== Vinyl DJ ===")
    print("Available genres: Alternative, Disco, Pop, Rock, RnB, Rap, Dance, Funk, Soul")
    print("Available moods: Happy, Lonely, Groovy, Cool, Bold, Chill, Energy \n")

    while True:
        user_input = input("Enter a favorite genre or your mood (or type 'quit' to exit): ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # 4. Receives either a single song dictionary or None
        song = recommend_music(user_input)

        if song:
            print("\nTake this record for a spin:")
            # 5. Fixed: Removed loop and added missing closing visual bracket ']'
            print(f" 💿 '{song['title']}' by {song['artist']} [{song['genres']}] [{song['moods']}]\n")
        else:
            print("\nSorry, we found no matches for that preference. Try another genre or mood.\n")

if __name__ == "__main__":
    main()
