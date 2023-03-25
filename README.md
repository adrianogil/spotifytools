# SpotifyTools

SpotifyTools is a collection of Python scripts for interacting with the Spotify Web API.

## Installation

1.  Clone this repository: `git clone https://github.com/yourusername/spotifytools.git`
2.  Install the required dependencies: `pip install -r src/requirements.txt`
3.  Add the following lines to your bashrc:
```
export SPOTIFY_TOOLS_DIR=<path-to-spotifytools>
source $SPOTIFY_TOOLS_DIR/src/bashrc.sh
```

## Usage

### `get_last_listened_songs.py`

This script displays a list of the user's recently played tracks, including the track name and artist name(s).

`python -m spotifytools.cli.get_last_listened_songs`

## Authentication

Before running any of the scripts, you must set your Spotify API credentials in a `config.ini` file in the root directory of the project:


`[spotify] client_id = YOUR_CLIENT_ID client_secret = YOUR_CLIENT_SECRET redirect_uri = YOUR_REDIRECT_URI`

You can obtain your client ID and client secret by creating a new Spotify app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/). The redirect URI should be set to `http://localhost:8888/callback` if you plan to use the built-in authentication flow.

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.
