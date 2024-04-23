from Commands.Command import Command
from Memory import Memory

class RecallCommand(Command):
    def __init__(self):
        pass

    def run(self, args: list[str], mem: Memory) -> str:
        return mem.get(args[0])