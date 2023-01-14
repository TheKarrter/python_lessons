# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя
#

num_list = [5, 3, 8, 12, 16, 16, 10, 32, 1, 2, 3, 5, 7]

# print(num_list)
# min_num = num_list[0]

# def nextmax(my_list):                 #Не оптимизирован
#     maxx = my_list[0]
#     res = [my_list[0]]
#     for i in range(len(my_list)):
#         if my_list[i] > maxx:
#             maxx = my_list[i]
#             res.append(maxx)
#     return res

# print(nextmax(num_list))

res = [num_list[0]]                     #list_comprehantion
[res.append(item) for item in num_list if item > res[-1]]
print(res)