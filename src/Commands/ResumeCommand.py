from Memory import Memory
import spotipy

class ResumeCommand:
    def __init__(self, spotifyObject: spotipy.Spotify):
        self.__spotifyObject = spotifyObject

    def run(self, args: list[str], mem: Memory) -> str:
        devices = self.__spotifyObject.devices()['devices']
        device = None
        for d in devices:
            if d['type'] == 'Computer':
                device = d
                break

        if device is None:
            return 'Error: Computer not active!'

        device_id = device['id']
        self.__spotifyObject.start_playback(device_id=device_id)