import requests
from bs4 import BeautifulSoup


dict = {}

class Horoscope:
    def __init__(self, mark, day='today'):
        self.mark = mark
        self.day = day

    def get_predict(self):
        working_url = f'https://horo.mail.ru/prediction/{self.mark}/{self.day}/'
        print(working_url)
        res = requests.get(working_url)
        soup = BeautifulSoup(res.content, 'html.parser')
        header = soup.find('h1', attrs= {'class': "hdr__inner"})
        data = soup.find('div', attrs={'class': 'article__item article__item_alignment_left article__item_html'})
        dict[self.mark] = header.text + " ☯ " + "\n" + data.text.replace('\n',' ')
        return dict

# taurus = Horoscope(mark = 'capricorn')
# print(taurus.get_predict())
