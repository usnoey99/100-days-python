## Day 46 - Musical Time Machine Project

---

### 📌 Overview

Building a musical time machine using web scraping and the Spotify API.

Scraping the Billboard Hot 100 chart for a specific date using BeautifulSoup, extracting the top 100 song titles, and creating a Spotify playlist based on that date. Using the Spotify API to search for each song and automatically add them to a new playlist.

---

### 📝 Tasks

* Scrape the Billboard Hot 100 chart using BeautifulSoup
* Extract song titles from a specific date
* Learn how Spotify API authentication works
* Search for songs using the Spotify API
* Create a new Spotify playlist
* Add songs to the playlist automatically
* Build a musical time machine project



---

## 🧠 Notes

### Spotify API

The Spotify API allows developers to access Spotify data and interact with Spotify features programmatically.

It can be used to search for tracks, retrieve user information, create playlists, and add songs to playlists.

### Spotipy

Spotipy is a lightweight Python library for working with the Spotify Web API.

It simplifies authentication and API requests, making it easier to interact with Spotify from Python.

Example:

```python
import spotipy

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(...))
```

### OAuth Authentication

OAuth is an authorization framework that allows applications to access user data without handling the user's password directly.

Spotify uses OAuth to verify user identity and grant permissions to applications.

### SpotifyOAuth

`SpotifyOAuth` handles the Spotify authentication flow and manages access tokens automatically.

Example:

```python
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private"
    )
)
```

### Scope

A scope defines the permissions requested by an application.

For example:

```python
scope="playlist-modify-private"
```

This scope allows the application to create and modify private playlists.

### Spotify URI

A Spotify URI is a unique identifier for Spotify content such as tracks, albums, artists, and playlists.

Example:

```text
spotify:track:4cOdK2wGLETKBW3PvgPWqT
```

URIs are commonly used when adding songs to playlists.

### search()

The `search()` method searches Spotify for tracks, albums, artists, playlists, and more.

Example:

```python
result = sp.search(
    q="track:Shape of You artist:Ed Sheeran",
    type="track"
)
```

### current_user()

The `current_user()` method retrieves information about the authenticated Spotify user.

Example:

```python
user_id = sp.current_user()["id"]
```

### user_playlist_create()

The `user_playlist_create()` method creates a new playlist for the authenticated user.

Example:

```python
playlist = sp.user_playlist_create(
    user=user_id,
    name="My Playlist",
    public=False
)
```

### playlist_add_items()

The `playlist_add_items()` method adds tracks to a Spotify playlist.

Example:

```python
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)
```

### try-except

The `try-except` statement is used to handle exceptions and prevent a program from crashing when errors occur.

Example:

```python
try:
    uri = result["tracks"]["items"][0]["uri"]
except IndexError:
    print("Track not found.")
```
