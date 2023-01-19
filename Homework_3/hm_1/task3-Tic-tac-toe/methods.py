board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def player_move(player_symbol):
    valid = False
    while not valid:
        player_number = input('Введите номер места в таблице от 1 до 9: ')
        try: 
            player_number = int(player_number)
        except: 
            print("Некорректный ввод. Введите, пожалуйста, число")
            continue
        if player_number >= 1 and player_number <= 9:
         if(str(board[player_number-1]) not in "XO"):
            board[player_number-1] = player_symbol
            valid = True
         else:
            print("Эта клетка уже занята!")
        else:
            print('Некорректный ввод. Введите число от 1 до 9!')
            
def win_check(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           player_move("X")
        else:
           player_move("O")
        counter += 1
        if counter > 4:
           tmp = win_check(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")