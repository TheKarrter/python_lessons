#1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
num_list = [1, 4, 12, 3, 9, 6, 11, 5, 4, 4, 7]
sum = 0

for i in range(0,len(num_list)):
    if i % 2 != 0: sum += num_list[i]

print(sum)
