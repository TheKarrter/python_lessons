# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите n: '))

n_list = []
sum = 0
for i in range (1, n+1):
    i = (1+1/i)**i
    sum += i
    n_list.append(round(i,2))
print(n_list)
print(round(sum, 2))