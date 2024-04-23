from Commands.Command import Command
from Memory import Memory

class SpeakCommand(Command):
    def __init__(self, speak_engine):
        self.__engine = speak_engine

    def run(self, args: list[str], mem: Memory) -> str:
        self.__engine.say(args[0])
        self.__engine.runAndWait()
        # return args[0]