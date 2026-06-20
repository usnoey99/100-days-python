import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id ="USER_UNIQuE_CLIENT_ID",
        client_secret="USER_UNIQuE_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)

# spotify searching
user_id = sp.current_user()["id"]

URL = "https://music.bugs.co.kr/chart/track/day/total?chartdate="

travel_date = input("Which year do you want to travel to?\n"
             "Type the date in this format YYYYMMDD: ")

response = requests.get(f"{URL}{travel_date}")

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all("tr", rowtype="track")

song_uris = []
hot100 = []

for song in songs:
    title = song.find("p", class_="title").find("a").getText()
    artist= song.find("p", class_="artist").find("a").getText()

    hot100.append({
        "title": title,
        "artist": artist
    })

for song in hot100:
    title = song["title"]
    artist = song["artist"]
    print(f"Searching: {title} - {artist}")
    try:

        result = sp.search(
            q=f"track:{title} artist:{artist}",
            type="track",
            limit=1
        )
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} by {artist} doesn't exist in Spotify. Skipped.")


# make a spotify playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{travel_date} Bugs Top 100",
    public=False
)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)