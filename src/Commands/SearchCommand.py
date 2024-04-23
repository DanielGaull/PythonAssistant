from Memory import Memory
from googlesearch import search
import requests
from bs4 import BeautifulSoup

class SearchCommand:
    def __init__(self):
        pass

    def run(self, args: list[str], mem: Memory) -> str:
        result = list(search(args[0], tld='co.in', num=1, stop=1, pause=2))[0]
        response = requests.get(result)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.get_text()
        return result