from random import randint
import methods

def player_vs_easy_bot():
    player_name = input('Введите свое имя: ')
    candies = 2021
    max_move = 28
    count_for_win_check = candies // max_move
    determing_move = randint(0,1)
    win = False
    while not win:
        if determing_move % 2 == 0:
            candies = methods.player_move(player_name, candies, max_move)
        else:
            candies = methods.easy_bot_move(candies, max_move)
        if determing_move >= count_for_win_check - 1:
            temp = methods.win_check(candies, determing_move, player_name, 'Easy bot')
            if temp:
                print(f'{temp} победил')
                win = True
        determing_move += 1

def player_vs_hard_bot():
    player_name = input('Введите свое имя: ')
    candies = 2021
    max_move = 28
    count_for_win_check = candies // max_move
    determing_move = randint(0,1)
    win = False
    while not win:
        if determing_move % 2 == 0:
            candies = methods.player_move(player_name, candies, max_move)
        else:
            candies = methods.hard_bot_move(candies, max_move)
        if determing_move >= count_for_win_check - 1:
            temp = methods.win_check(candies, determing_move, player_name, 'Hard bot')
            if temp:
                print(f'{temp} победил')
                win = True
        determing_move += 1

def player_vs_player():
    first_player_name = input('Введите имя первого игрока: ')
    second_player_name = input('Введите имя второго игрока: ')
    candies = 2021
    max_move = 28
    count_for_win_check = candies // max_move
    determing_move = randint(0,1)
    win = False
    while not win:
        if determing_move % 2 == 0:
            candies = methods.player_move(first_player_name, candies, max_move)
        else:
            candies = methods.player_move(second_player_name, candies, max_move)
        if determing_move >= count_for_win_check - 1:
            temp = methods.win_check(candies, determing_move, first_player_name, second_player_name)
            if temp: 
                print(f'{temp} победил')
                win = True
            determing_move += 1