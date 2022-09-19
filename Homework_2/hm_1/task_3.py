#3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
min_fraction = list[0]%1
max_fraction = list[0]%1

for i in range(0,len(list)):
    if list[i]%1 < min_fraction: min_fraction = list[i]%1
    if list[i]%1 > max_fraction: max_fraction = list[i]%1

print(max_fraction - min_fraction)
