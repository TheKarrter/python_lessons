# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 

n = int(input('Введите n: '))
n_list = []
for i in range(-n, n+1):
    n_list.append(i)
print(n_list)

mult = 1

ids_for_sum = input('Введите через пробел номера элементов, сумму которых вы хотите найти: ')
for i in ids_for_sum.split(' '):
    mult *= n_list[int(i)]
print(mult)