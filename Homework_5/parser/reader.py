from bs4 import BeautifulSoup
import requests

class Weather:
    def __init__(self,link):
        self.link = link
        request = requests.get(self.link).text
        self.soup = BeautifulSoup(request, 'html.parser')
    def get_cities(self):
        data = self.soup.find_all('a')
        links = {}
        for block in data:
            text = block.__str__()
            name = block.get_text()
            text = text[text.find('href="'):][6:]
            text = text[:text.find('"')]
            if name not in ('Мобильная версия', 'Главная', 'О сайте', 'Частые вопросы (FAQ)', 'Контакты','Литва', 'Беларусь', 'Россия', 'Украина', 'Все страны', '>>>', 'См. на карте','Посмотреть',' 21 сент. 2023' ''):
                links[name] = "https://rp5.ru" + text
        return links

