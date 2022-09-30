import telebot
from random import *
import json
import requests


films = []

API_URL = "https://7012.deeppavlov.ai/model"

def save():
    with open("films.json", 'w', encoding = 'utf-8') as fh:
        fh.write(json.dumps(films, ensure_ascii = False))
    print('Наша фильмотека была успешно сохранена в файле films.json')

def load():
    global films
    with open("films.json", "r", encoding = 'utf-8') as fh:
        films = json.load(fh)
    print('Фильмотека была успешно загружена')


API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_massage(message):
    try:
        load()
        bot.send_message(message.chat.id, 'Фильмотека была успешно загружена')
    except:
        films.append('Матрица')
        films.append('Солярис')
        films.append('Хакеры')
        films.append('Властелин колец')
        films.append('Техасская резня бензопилой')
        films.append('Санта барбара')
        bot.send_message(message.chat.id, 'Фильмотека была загружена по умолчанию')

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, 'Список фильмов:')
    bot.send_message(message.chat.id, ', '.join(films))

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.send_message(message.chat.id, 'Серега, тут мануал добавь, чтоб понятно было')

@bot.message_handler(commands=['add'])
def add_film(message):
    bot.send_message(message.chat.id, 'Название фильма, который вы хотите добавить: ')

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = ' '.join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json = data, verify = False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat,id, 'Что-то я ничего не нашел')

bot.polling()

# while True:
#     command = input("Введите команду: ")
#     if command == "/start":
#         print("Бот с фильмами начал свою работу!")
#     elif command == "/stop":
#         print("Бот закончил работу")
#         break
#     elif command == "/showfilms":
#         print('Текущий список фильмов: ')
#         print(films)
#     elif command == "/add":
#         films.append(input('Введите название фильма: '))
#         print("Фильм был успешно добавлен в коллекцию!")
#     elif command == "/help":
#         print('Серега, тут мануал добавь, чтоб понятно было')
#     elif command == "/del":
#         try:
#             films.remove(input('Введите название фильма, который вы котите удалить: '))
#             print('Фильма был успешно удален!')
#         except: print('Такого фильма нет в фильмотеке!')
#     elif command == '/random':
#         # print('Слепой жребий показал вам:',films[randint(0,len(films)-1)])
#         print('Слепой жребий показал вам:', choice(films))
#     elif command == '/save':
#         save()
#     elif command == '/load':
#         with open("films.json", 'r', encoding = 'utf-8') as fh:
#             films = json.load(fh)
#         print('Наша фильмотека была успешно загружена из файла films.json')
#     else: 
#         print("Неопознаянная команда. Просьба изучить мануал через /help")