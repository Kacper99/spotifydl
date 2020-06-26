# Spotify Downloader
Download all the songs from your spotify playlist using youtube-dl

## How to use
This program requires [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html) 
and [ffmpeg](https://www.ffmpeg.org). On MacOS these can be easily installed using 
[homebrew](https://brew.sh).

Make sure you install all the required packages from the requirements.txt which can be 
done using the `pip install -r requirements.txt`

You *need* to create an app on the Spotify developer [website](https://developer.spotify.com/dashboard/applications) 
to obtain a client ID and a client secret which have to be passed in through command
line arguments. Once you obtain these run the downloader with the command
`python3 spotifydl.py --id 00000000000 --secret 0000000000` (replace with your
own key and secret).  

Once you run the program in your terminal, you will be asked for the username of the
author of the playlist, the playlist URI, and the save destination. These can also be
passed in through the command line:
`--id 00000 --secret 000000 -c --username user --playlist_uri "spotify:playlist:xxxxxxxxxxxxxx" --dir "~/desination-dir"`

## Command line arguments
```bash
usage: Download your spotify playlist through youtubedl [-h] [--id ID]
                                                        [--secret SECRET] [-c]
                                                        [--username USERNAME]
                                                        [--playlist_uri PLAYLIST_URI]
                                                        [--dir DIR]

optional arguments:
  -h, --help            show this help message and exit
  --id ID               Spotify client ID
  --secret SECRET       Spotify client secret
  -c                    If you want to pass the username and playlist ID using
                        command line use this
  --username USERNAME   Username of the authors playlist
  --playlist_uri PLAYLIST_URI
                        URI of the playlist
  --dir DIR             Save destination directory
```