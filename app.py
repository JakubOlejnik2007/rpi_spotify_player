import spotipy
from spotipy.oauth2 import SpotifyOAuth

auth = SpotifyOAuth(
    client_id="68f4a84950014252afb2201862661e41",
    client_secret="1b5b37e516c84653ab695bc169dad1df",
    redirect_uri="http://127.0.0.1:8080/callback",
    scope="user-modify-playback-state user-read-playback-state",
    cache_path=".cache"
)

sp = spotipy.Spotify(auth_manager=auth)
devices = sp.devices()["devices"]
print(devices)


curr_device = devices[0]

sp.next_track(curr_device["id"])

print(sp.current_playback())