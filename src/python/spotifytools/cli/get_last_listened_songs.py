from spotifytools.songs.last_listened_songs import get_recently_played_tracks


if __name__ == '__main__':
    recently_played = get_recently_played_tracks()
    for idx, track in enumerate(recently_played):
        track_genres_str = ", ".join([artist.get('genres', '') for artist in track['artists']])
        print(idx, '-', track['song'], "by", ", ".join([artist['name'] for artist in track['artists']]), "({})".format(track_genres_str))
