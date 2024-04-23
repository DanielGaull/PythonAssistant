from Assistant import Assistant
from Memory import Memory


def main():
    assistant = Assistant()
    mem = Memory()
    mem.load_from_file('mem.txt')
    vars = Memory()
    print('Welcome to the Assistant Terminal')
    while True:
        line = input('> ')
        assistant.run_line(line, mem, vars)
#     assistant.run_block('''
#     x = recall "favorite_song"
#     play "{x}"
#     ''')

main()