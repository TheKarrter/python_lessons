#3) Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
list1 = [1, 1, 2, 3, 4, 5, 5]
list2 = []

for i in list1:
    k = 0
    for j in list1:
        if i == j: k+=1
    if k == 1: list2.append(i)

print(list2)