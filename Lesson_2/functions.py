def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

def new_string(symbol, count = 3):
    return symbol * count

def concatenation(*params):
    res: str = ""
    for item in params:
        res += item
    return res

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)