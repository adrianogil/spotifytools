import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

scope = "user-read-recently-played"
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

today = datetime.now()
yesterday = today.replace(hour=0, minute=0, second=0, microsecond=0)
results = sp.current_user_recently_played(after=int(yesterday.timestamp() * 1000))

for idx, item in enumerate(results['items']):
    track = item['track']
    artists_str = ''
    for artist_short_data in track['artists']:
        artist_full_data = sp.artist(artist_short_data['uri'])
        if artists_str:
            artists_str += ', '
        if artist_full_data['genres']:
            artists_str += artist_full_data['name'] + " (%s)" % (", ".join(artist_full_data['genres']),)
        else:
            artists_str += artist_full_data['name']
    print(idx, track['name'], "by", artists_str)
