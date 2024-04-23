from Assistant import Assistant


def main():
    assistant = Assistant()
    assistant.run_block('''
    x = recall "favorite_song"
    play "{x}"
    ''')

main()