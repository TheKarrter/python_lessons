import telebot
from random import *
import json




# def save():
#     with open("films.json", 'w', encoding = 'utf-8') as fh:
#         fh.write(json.dumps(films, ensure_ascii = False))
#     print('Наша фильмотека была успешно сохранена в файле films.json')
films = []
        
API_TOKEN ='5653912088:AAEdoH0JFcjdbhs6DZU6VkensUORyjw5pwg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_massage(message):
    films.append('Матрица')
    films.append('Солярис')
    films.append('Хакеры')
    films.append('Властелин колец')
    films.append('Техасская резня бензопилой')
    films.append('Санта барбара')
    bot.send_message(message.chat.id, 'Привет, я заработал')

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, 'Список фильмов: ', films)

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