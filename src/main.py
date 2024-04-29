from Assistant import Assistant
from Memory import Memory
from Microphone import Microphone

def run_cli(assistant):
    mem = Memory()
    mem.load_from_file('mem.txt')
    vars = Memory()
    print('Welcome to the Assistant Terminal')
    while True:
        line = input('> ')
        res = assistant.run_line(line, mem, vars)
        print(res)

def main():
    # assistant = Assistant()
    # run_cli(assistant)
    mic = Microphone()
    while True:
        print('Listening...')
        text = mic.listen()
        print(text)


    # assistant.run_block('''
    # x = recall "favorite_song"
    # play "{x}"
    # ''')

main()