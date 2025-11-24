import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk

scope = "user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="68f4a84950014252afb2201862661e41",
    client_secret="1b5b37e516c84653ab695bc169dad1df",
    redirect_uri="https://127.0.0.1/",
    scope=scope,
    cache_path=".cache"
))

devices = sp.devices()
for d in devices['devices']:
    print(d['name'], d['id'])

device_id = next(d['id'] for d in devices['devices'] if d['name'] == "Kolumna (salon)")

def play():
    sp.start_playback(device_id=device_id)

def pause():
    sp.pause_playback(device_id=device_id)

root = tk.Tk()
root.attributes("-fullscreen", True)

tk.Button(root, text="Play", command=play, width=20, height=5).pack()
tk.Button(root, text="Pause", command=pause, width=20, height=5).pack()

root.mainloop()
