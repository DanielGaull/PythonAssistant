from Memory import Memory
import json
import spotipy
import webbrowser

class PlayCommand:
    def __init__(self, id, secret, username, redirect_uri, code):

        oauth_object = spotipy.SpotifyOAuth(id, secret, redirect_uri, 
                    scope="user-read-playback-state,user-modify-playback-state")
        token_dict = oauth_object.get_access_token(code=code) 
        token = token_dict['access_token'] 
        self.__spotifyObject = spotipy.Spotify(auth=token)

    def run(self, args: list[str], mem: Memory) -> str:
        results = self.__spotifyObject.search(args[0], 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        uri = song_items[0]['uri']
        devices = self.__spotifyObject.devices()['devices']
        device = None
        for d in devices:
            if d['type'] == 'Computer':
                device = d
                break

        if device is None:
            return 'Error: Computer not active!'

        device_id = device['id']
        self.__spotifyObject.start_playback(uris=[uri], device_id=device_id)
        