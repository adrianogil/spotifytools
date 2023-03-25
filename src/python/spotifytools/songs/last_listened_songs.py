import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from datetime import datetime


def get_recently_played_tracks():
    # sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    scope = "user-read-recently-played"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    today = datetime.now()
    yesterday = today.replace(hour=0, minute=0, second=0, microsecond=0)
    results = sp.current_user_recently_played(after=int(yesterday.timestamp() * 1000))
    tracks = []
    for item in results['items']:
        track = item['track']
        artists = []
        for artist_short_data in track['artists']:
            artist_full_data = sp.artist(artist_short_data['uri'])
            artist = {'name': artist_full_data['name']}
            if artist_full_data['genres']:
                artist['genres'] = ", ".join(artist_full_data['genres'])
            artists.append(artist)
        track_info = {'song': track['name'], 'artists': artists}
        tracks.append(track_info)
    return tracks
