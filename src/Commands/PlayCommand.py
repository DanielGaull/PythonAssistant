from Memory import Memory
import spotipy

class PlayCommand:
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
        
        results = self.__spotifyObject.search(args[0], 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        uri = song_items[0]['uri']

        self.__spotifyObject.start_playback(uris=[uri], device_id=device_id)
        
    # Too slow
    # def __get_all_tracks(self):
    #     def track_to_simple(track):
    #         track = track['track']
    #         name = track['name'] + ' by ' + track['artists'][0]['name']
    #         return {'name': name, 'uri': track['uri']}
    #     resp = self.__spotifyObject.current_user_saved_tracks(limit=50)
    #     total = resp['total']
    #     tracks = list(map(track_to_simple, resp['items']))
    #     offset = 0
    #     while offset < total:
    #         resp = self.__spotifyObject.current_user_saved_tracks(limit=50, offset=offset)
    #         offset = offset + 50
    #         print('Done, next offset', offset)
    #     print('done!', len(tracks))
    #     return tracks