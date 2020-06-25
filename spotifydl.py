import spotipy
import spotipy.oauth2 as oauth2
import argparse


def get_args():
    parser = argparse.ArgumentParser('Download your spotify playlist through youtubedl')
    parser.add_argument('--id', metavar='ID', help='Spotify client ID')
    parser.add_argument('--secret', metavar='Client', help='Spotify client secret')
    parser.add_argument('-c', action='store_true',
                        help='If you want to pass the username and playlist ID using command line use this')
    parser.add_argument('--username', metavar='Username', help='Username of the authors playlist')
    parser.add_argument('--playlist_uri', metavar='PlaylistURI', help='URI of the playlist')
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
    if args.c is True:
        songs = get_track_names(spotify, args.username, args.playlist)
    else:
        username = input('Spotify Username')
        playlist_uri = input('Spotify playlist URI')
        songs = get_track_names(spotify, username, playlist_uri)

    print(songs)




