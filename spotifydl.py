import spotipy
import spotipy.oauth2 as oauth2
import argparse
import os
import multiprocessing
from downloader import Downloader
from itertools import product


save_dir = '/'


def get_args():
    parser = argparse.ArgumentParser('Download your spotify playlist through youtubedl')
    parser.add_argument('--id', help='Spotify client ID')
    parser.add_argument('--secret', help='Spotify client secret')
    parser.add_argument('-c', action='store_true',
                        help='If you want to pass the username and playlist ID using command line use this')
    parser.add_argument('--username', help='Username of the authors playlist')
    parser.add_argument('--playlist_uri', help='URI of the playlist')
    parser.add_argument('--dir', help='Save destination directory')
    return parser.parse_args()


def generate_token(id, secret):
    credentials = oauth2.SpotifyClientCredentials(
        client_id=id,
        client_secret=secret)
    return credentials.get_access_token(as_dict=False)


def get_playlist_tracks(S, username, playlist_id):
    results = S.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = S.next(results)
        tracks.extend(results['items'])
    return tracks


def get_track_names(S, username, playlist_id):
    tracks = get_playlist_tracks(S, username, playlist_id)
    print('Found {} tracks'.format(len(tracks)))
    song_names = []
    for track in tracks:
        track = track['track']
        song_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        song_names.append((song_name, artists))
    return song_names


if __name__ == '__main__':
    args = get_args()
    token = generate_token(args.id, args.secret)

    spotify = spotipy.Spotify(auth=token)

    songs = None
    if args.c is False:
        args.username = input('Spotify Username (e.g. johndoe123):\n')
        args.playlist_uri = input('Spotify playlist URI (e.g. spotify:playlist:xxxxxxxxxxxxxxxxxxxxxx):\n')
        args.dir = input('Save directory (e.g. ~/Desktop/Summer Tunes 2020):\n')

    songs = get_track_names(spotify, args.username, args.playlist_uri)
    dl = Downloader(args.dir)
    pool = multiprocessing.Pool(5)
    pool.map(dl.download_song, songs)
