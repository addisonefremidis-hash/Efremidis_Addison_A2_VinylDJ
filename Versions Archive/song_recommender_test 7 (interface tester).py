import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  

# A hardcoded database of records
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
    {"title": "Tell it to my Heart", "artist": "Taylor Dayne", "genres": "Pop", "moods": "Happy"},
    {"title": "Footloose", "artist": "Mixed Artists", "genres": "Dance Pop", "moods": "Groovy"},
    {"title": "Saturday Night Fever", "artist": "Mixed Artists", "genres": "Disco Dance", "moods": "Groovy"},
    {"title": "Sensational 70's", "artist": "Mixed Artists", "genres": "Soul Funk", "moods": "Groovy"},
]

# Drop down lists
OPTIONS = [
    "-- GENRES --", "Alternative", "Disco", "Dance", "Funk", "Pop", "Rap", "Rock", "RnB", "Soul",
    "-- MOODS --", "Bold", "Chill", "Cool", "Energy", "Groovy", "Happy", "Lonely", "Sad"
]

def handle_recommendation():
    """Reads the chosen drop-down item and fetches a random match."""
    preference = options_dropdown.get().strip().lower()
    
    # Validation if they click the button on a placeholder banner or empty selection
    if not preference or "---" in preference:
        messagebox.showwarning("Selection Error", "Please pick a valid Genre or Mood from the drop-down menu!")
        return

    matches = []
    for song in MUSIC_DATABASE:
        if preference in song["genres"].lower() or preference in song["moods"].lower():
            matches.append(song)

    if matches:
        song = random.choice(matches)
        result_title_label.config(text=f" 💿 \"{song['title']}\"")
        result_artist_label.config(text=f"by {song['artist']}")
        result_tags_label.config(text=f"[{song['genres']}]  •  [{song['moods']}]")
    else:
        result_title_label.config(text="")
        result_artist_label.config(text="")
        result_tags_label.config(text="")
        messagebox.showinfo("No Matches", "No matching tracks available right now.")

# --- UI Setup ---
root = tk.Tk()
root.title("Vinyl DJ")
root.geometry("700x650")
root.config(bg="#F0731F")

# Header Label
header_label = tk.Label(root, text="=== Vinyl DJ ===", font=("Impact", 38, "bold"), fg="#337CA6", bg="#F0731F")
header_label.pack(pady=10)

# Instructions Label
instruction_label = tk.Label(root, text="Select your desired sounds or vibe:", font=("Arial", 20), fg="#ffffff", bg="#56C1C4")
instruction_label.pack(pady=5)

# 2. Combobox Menu (Replaced tk.Entry)
options_dropdown = ttk.Combobox(root, values=OPTIONS, font=("Arial", 21), width=32, state="readonly")
options_dropdown.set("Select Genre or Mood...")  # Default placeholder text
options_dropdown.pack(pady=5)

# Recommendation Button
submit_button = tk.Button(root, text="Spin Record ⚡", font=("Impact", 21, "bold"), bg="#ff9f1c", fg="#337CA6", command=handle_recommendation, cursor="hand2")
submit_button.pack(pady=15)

# Visual Frame for the Result Output
output_frame = tk.Frame(root, bg="#337CA6")
output_frame.pack(pady=10, fill="x")

result_title_label = tk.Label(output_frame, text="", font=("Arial", 24, "bold"), fg="#cbf3f0", bg="#337CA6")
result_title_label.pack()

result_artist_label = tk.Label(output_frame, text="", font=("Arial", 22, "italic"), fg="#ffffff", bg="#337CA6")
result_artist_label.pack()

result_tags_label = tk.Label(output_frame, text="", font=("Arial", 19), fg="#ffffff", bg="#337CA6")
result_tags_label.pack(pady=5)

root.mainloop()
