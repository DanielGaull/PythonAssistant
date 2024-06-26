import typing
import shlex
from Commands.PauseCommand import PauseCommand
from Commands.PlayCommand import PlayCommand
from Commands.ResumeCommand import ResumeCommand
from Commands.SearchCommand import SearchCommand
from Memory import Memory
from Commands.SpeakCommand import SpeakCommand
from Commands.RememberCommand import RememberCommand
from Commands.RecallCommand import RecallCommand
from dotenv import dotenv_values

import re
import pyttsx3
import spotipy

class Assistant:
    def __init__(self):
        env = dotenv_values(".env")

        oauth_object = spotipy.SpotifyOAuth(env['sp_client_id'], env['sp_client_secret'], env['sp_redirect_uri'], 
                    scope="user-read-playback-state,user-modify-playback-state,user-library-read")
        token_dict = oauth_object.get_access_token()#code=env['sp_code']) 
        token = token_dict['access_token'] 
        spotifyObject = spotipy.Spotify(auth=token)

        self.__engine = pyttsx3.init()
        self.__cmd_dict = {'speak': SpeakCommand(self.__engine),
                           'remember': RememberCommand(),
                           'recall': RecallCommand(),
                           'play': PlayCommand(spotifyObject),
                           'pause': PauseCommand(spotifyObject),
                           'resume': ResumeCommand(spotifyObject),
                           'search': SearchCommand()
                           }

    def __replace_vars(self, s: str, vars: Memory) -> str:
        for k in vars.keys():
            repl = '{' + k + '}'
            s = s.replace(repl, vars.get(k))
        return s

    def __run_cmd(self, command: str, mem: Memory, vars: Memory):
        space_index = command.find(' ')
        cmd_type = command[:space_index]
        if space_index < 0:
            cmd_type = command
        # Split args, but keep spaces if they're within quotes
        args = shlex.split(command[space_index + 1:])
        # Replace all variables with literal values in the arguments
        for i in range(len(args)):
            args[i] = self.__replace_vars(args[i], vars).strip()

        return self.__cmd_dict[cmd_type].run(args, mem)

    def run_line(self, line: str, mem: Memory, vars: Memory):
        if line.startswith('#'):
            return

        match = re.match(r'^([a-zA-Z][a-zA-Z0-9]*)(?:\s)*=(?:\s)*(.*)$', line)
        if match:
            # This is a variable assignment line
            groups = match.groups()
            var_name = groups[0]
            cmd = groups[1]
            cmd_value = self.__run_cmd(cmd, mem, vars)
            vars.put(var_name, cmd_value)
        else:
            return self.__run_cmd(line, mem, vars)

    def run_block(self, code: str):
        mem = Memory()
        mem.load_from_file('mem.txt')

        vars = Memory()
        lines = code.splitlines()
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                return_val = self.run_line(line, mem, vars)
                if return_val is not None:
                    self.__run_cmd('speak ' + return_val)