# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя
#

num_list = [5, 3, 8, 12, 16, 10, 32, 1, 2, 3, 5, 7]
num_list2 = []

# print(num_list)
# min_num = num_list[0]

def nextmax(list):
    max = list[0]
    res = [list[0]]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            res.append(max)
    return res

print(nextmax(num_list))