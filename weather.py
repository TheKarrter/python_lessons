from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from parse import *
import requests

URL = 'https://world-weather.ru/pogoda/russia/kungur/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "lxml")

temp = bs.find('div', class_ = 'weather-now-number')

print(bs)