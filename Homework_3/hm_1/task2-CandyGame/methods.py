from random import randint

def player_move(player_name, candies, max_move):
    valid = False
    while not valid:
        move = input(f'{player_name}, ваш ход ')
        try:
            move = int(move)
            if move > 0 and move <= max_move and move <= candies:
                print(f'Вы забрали {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                valid = True
            else:
                print(f'Кол-во конфет должно быть в интервале от 1 до {max_move} или не больше оставшегося количества конфет')
        except:
            print('Необходимо ввести целое число')
    return candies

def easy_bot_move(candies, max_move):
    move = randint(1,max_move) if candies >= max_move else randint(1, candies)
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

def hard_bot_move(candies, max_move):
    move = candies % (max_move + 1)
    if move == 0:
        move = randint(1, max_move) if max_move <= candies else candies
        print(f'Бот забрал {move} конфет')
        candies -= move
        print(f'Осталось {candies} конфет')
        return candies

def win_check(candies, determing_move, first_player, second_player):
    if candies == 0:
        return first_player if determing_move % 2 == 0 else second_player
    else:
        return False
