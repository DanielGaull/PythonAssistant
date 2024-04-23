from Memory import Memory
import spotipy

class PlayCommand:
    def __init__(self, spotifyObject: spotipy.Spotify):
        self.__spotifyObject = spotifyObject

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
        