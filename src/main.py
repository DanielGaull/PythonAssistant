from Assistant import Assistant
from Memory import Memory

def run_cli(assistant):
    mem = Memory()
    mem.load_from_file('mem.txt')
    vars = Memory()
    print('Welcome to the Assistant Terminal')
    while True:
        line = input('> ')
        assistant.run_line(line, mem, vars)

def main():
    assistant = Assistant()
    run_cli(assistant)


    # assistant.run_block('''
    # x = recall "favorite_song"
    # play "{x}"
    # ''')

main()