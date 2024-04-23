from Commands.Command import Command
from Memory import Memory

class RememberCommand(Command):
    def __init__(self):
        pass

    def run(self, args: list[str], mem: Memory) -> str:
        mem.put(args[0], args[1])
        mem.save()