from Memory import Memory
import json
import spotipy
import webbrowser

class PlayCommand:
    def __init__(self, id, secret, username, redirect_uri, code):

        oauth_object = spotipy.SpotifyOAuth(id, secret, redirect_uri)
        token_dict = oauth_object.get_access_token(code=code) 
        token = token_dict['access_token'] 
        self.__spotifyObject = spotipy.Spotify(auth=token)
        #user_name = spotifyObject.current_user()
        #print(json.dumps(user_name, sort_keys=True, indent=4))

    def run(self, args: list[str], mem: Memory) -> str:

        

        pass