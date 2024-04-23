from Assistant import Assistant


def main():
    assistant = Assistant()
    assistant.run_block('''
    x = recall "favorite_color"
    speak "Your favorite color is {x}"
    ''')

main()