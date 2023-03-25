if [ -z "$SPOTIFY_TOOLS_PYTHON_DIR" ]
then
    export SPOTIFY_TOOLS_PYTHON_DIR=$SPOTIFY_TOOLS_DIR/src/
    export PYTHONPATH=$SPOTIFY_TOOLS_PYTHON_DIR:$PYTHONPATH
fi


function spotify-get-last-listened-songs()
{
	python3 -m spotifytools.cli.get_last_listened_songs
}
