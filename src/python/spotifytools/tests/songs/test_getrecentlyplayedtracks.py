import unittest
from spotifytools.songs.last_listened_songs import get_recently_played_tracks

class TestGetRecentlyPlayedTracks(unittest.TestCase):

    def test_get_recently_played_tracks(self):
        tracks = get_recently_played_tracks()
        self.assertTrue(isinstance(tracks, list))
        self.assertTrue(len(tracks) > 0)
        for track in tracks:
            self.assertTrue(isinstance(track, dict))
            self.assertTrue('song' in track)
            self.assertTrue(isinstance(track['song'], str))
            self.assertTrue('artists' in track)
            self.assertTrue(isinstance(track['artists'], list))
            for artist in track['artists']:
                self.assertTrue(isinstance(artist, dict))
                self.assertTrue('name' in artist)
                self.assertTrue(isinstance(artist['name'], str))
                if 'genres' in artist:
                    self.assertTrue(isinstance(artist['genres'], str))

if __name__ == '__main__':
    unittest.main()
