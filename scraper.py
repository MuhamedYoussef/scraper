from bs4 import BeautifulSoup
import requests
import yaml


class Scraper:
    """ Simple web scraper """

    def __init__(self):
        return
    
    def parse_content(self, r):
        self.soup = BeautifulSoup(r.text, 'html.parser')
        print(f'\nPage title: {self.soup.title.string}')

    def get_links(self):
        links = self.soup.find_all('a')
        for link in links:
            print(link.get('href'))
    





if __name__ == "__main__":
    with open('data.yaml', 'r') as f:
        data = yaml.safe_load(f)
        print(data['banner'])
    
    scaper = Scraper()

    while True:
        url = input('Enter URL: ')
        try:
            r = requests.get(url)
            scaper.parse_content(r)
            break
        except:
            print('\nNot a valid url, try again!')

    
    while True:
        print(data['choices'])
        choice = input('Choice: ')
        if choice == str(1):
            scaper.get_links()
        elif choice.lower() == 'q':
            break
    
    print('Program ended!')