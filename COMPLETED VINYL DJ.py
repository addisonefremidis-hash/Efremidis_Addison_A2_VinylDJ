import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  

# A hardcoded database of records
MUSIC_DATABASE = [
    {"title": "Channel Orange", "artist": "Frank Ocean", "genres": "RnB", "moods": "Chill"},
    {"title": "Atavista", "artist": "Childish Gambino", "genres": "Rap RnB", "moods": "Chill"},
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
    {"title": "Tell it to my Heart", "artist": "Taylor Dayne", "genres": "Pop", "moods": "Happy"},
    {"title": "Footloose", "artist": "Mixed Artists", "genres": "Dance Pop", "moods": "Groovy"},
    {"title": "Saturday Night Fever", "artist": "Mixed Artists", "genres": "Disco Dance", "moods": "Groovy"},
    {"title": "Sensational 70's", "artist": "Mixed Artists", "genres": "Soul Funk", "moods": "Groovy"},
]

# Separate Dropdown Lists
# * Modified from: GeeksforGeeks (2020). Dropdown menus in Tkinter. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/dropdown-menus-tkinter/ [Accessed 15 Oct. 2026].
GENRES = ["-- ALL GENRES --", "Alternative", "Disco", "Dance", "Funk", "Pop", "Rap", "Rock", "RnB", "Soul"]
MOODS = ["-- ALL MOODS --", "Bold", "Chill", "Cool", "Energy", "Groovy", "Happy", "Lonely", "Sad"]

def handle_recommendation():
    """Reads both drop-down selections and fetches a random matching track."""
    genre_pref = genre_dropdown.get().strip().lower()
    mood_pref = mood_dropdown.get().strip().lower()
    
    genre_valid = genre_pref and "all genres" not in genre_pref
    mood_valid = mood_pref and "all moods" not in mood_pref

    # Validation if both are left unselected/placeholder
    if not genre_valid and not mood_valid:
        messagebox.showwarning("Selection Error", "Please pick at least a Genre or a Mood from the menus!")
        return

    matches = []
    for song in MUSIC_DATABASE:
        matches_genre = True
        matches_mood = True

        if genre_valid:
            matches_genre = genre_pref in song["genres"].lower()
        if mood_valid:
            matches_mood = mood_pref in song["moods"].lower()

        # Both active filters must match simultaneously
        if matches_genre and matches_mood:
            matches.append(song)

    if matches:
        song = random.choice(matches)
        # * Modified from:Python (2025). Random — Generate pseudo-random numbers — Python 3.8.2 documentation. [online] docs.python.org. Available at: https://docs.python.org/3/library/random.html 
        result_title_label.config(text=f" 💿 \"{song['title']}\"")
        result_artist_label.config(text=f"by {song['artist']}")
        result_tags_label.config(text=f"[{song['genres']}]  •  [{song['moods']}]")
    else:
        result_title_label.config(text="")
        result_artist_label.config(text="")
        result_tags_label.config(text="")
        messagebox.showinfo("No Matches", "No matching tracks available for this combination.")

# --- UI Setup ---
# * Modified from: Python(2019). Tkinter — Python interface to TCL/TK — Python 3.7.2 documentation. [online] python.org. Available at: https://docs.python.org/3/library/tkinter.html [Accessed 15 Oct. 2026].
root = tk.Tk()
root.title("Vinyl DJ")
root.geometry("700x720")
root.config(bg="#F0731F")

# Header Label
header_label = tk.Label(root, text="=== Vinyl DJ ===", font=("Impact", 38, "bold"), fg="#337CA6", bg="#F0731F")
header_label.pack(pady=10)

# Instructions Label
instruction_label = tk.Label(root, text="Select your desired genre and mood:", font=("Lexend", 18, "bold"), fg="#ffffff", bg="#56C1C4")
instruction_label.pack(pady=5)

# 1. Genre Combobox
genre_label = tk.Label(root, text="Genre:", font=("Lexend", 14, "bold"), fg="#ffffff", bg="#F0731F")
genre_label.pack(anchor="w", padx=110)
genre_dropdown = ttk.Combobox(root, values=GENRES, font=("Lexend", 16), width=32, state="readonly")
genre_dropdown.set("-- ALL GENRES --")
genre_dropdown.pack(pady=2)

# 2. Mood Combobox
mood_label = tk.Label(root, text="Mood:", font=("Lexend", 14, "bold"), fg="#ffffff", bg="#F0731F")
mood_label.pack(anchor="w", padx=110, pady=(10, 0))
mood_dropdown = ttk.Combobox(root, values=MOODS, font=("Lexend", 16), width=32, state="readonly")
mood_dropdown.set("-- ALL MOODS --")
mood_dropdown.pack(pady=2)

# Recommendation Button
submit_button = tk.Button(root, text="Spin Record ⚡", font=("Impact", 21, "bold"), bg="#ff9f1c", fg="#56C1C4", command=handle_recommendation, cursor="hand2")
submit_button.pack(pady=20)

# Visual Frame for the Result Output
output_frame = tk.Frame(root, bg="#337CA6")
output_frame.pack(pady=10, fill="x")

result_title_label = tk.Label(output_frame, text="", font=("Lexend", 22, "bold"), fg="#cbf3f0", bg="#337CA6")
result_title_label.pack()

result_artist_label = tk.Label(output_frame, text="", font=("Lexend", 20, "italic"), fg="#ffffff", bg="#337CA6")
result_artist_label.pack()

result_tags_label = tk.Label(output_frame, text="", font=("Lexend", 17), fg="#ffffff", bg="#337CA6")
result_tags_label.pack(pady=5)

root.mainloop()
