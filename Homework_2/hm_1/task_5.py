#5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
def fib(n):
    if n >= 0:
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        else: return fib(n-1) + fib(n-2)
    else:
        if n == -1: return 1
        elif n == -2: return -1
        else: return fib(n+2) - fib(n+1)

fib_list = []
k = 10

for i in range (-k, k+1):
    fib_list.append(fib(i))

print(fib_list)