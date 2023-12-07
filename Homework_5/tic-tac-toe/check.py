import variables as v
def win(symbol):
    if v.FIELD[0][0]==v.FIELD[0][1]==v.FIELD[0][2]==symbol:
        print(f'{symbol} has won')
        return True
    elif v.FIELD[1][0]==v.FIELD[1][1]==v.FIELD[1][2]==symbol:
        print(f'{symbol} has won')
        return False
    elif v.FIELD[2][0]==v.FIELD[2][1]==v.FIELD[2][2]==symbol:
        print(f'{symbol} has won')
        return True
    elif v.FIELD[0][0]==v.FIELD[1][0]==v.FIELD[2][0]==symbol:
        print(f'{symbol} has won')
        return True
    elif v.FIELD[0][1]==v.FIELD[1][1]==v.FIELD[2][1]==symbol:
        print(f'{symbol} has won')
        return True
    elif v.FIELD[0][2]==v.FIELD[1][2]==v.FIELD[2][2]==symbol:
        print(f'{symbol} has won')
        return True
    elif v.FIELD[0][0]==v.FIELD[1][1]==v.FIELD[2][2]==symbol:
        print(f'{symbol} has won')
        return True
    elif v.FIELD[0][2]==v.FIELD[1][1]==v.FIELD[2][1]==symbol:
        print(f'{symbol} has won')
        return True
    else:
        return False