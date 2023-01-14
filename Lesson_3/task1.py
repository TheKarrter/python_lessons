# В ФАЙЛЕ находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнить условие A[i] - 1 = A[i-1]
# Найдите это число


# def fun(num):                             #Способ не оптимизированный
#     for i in range(1,len(num)):
#         if num[i] - 1 != num[i-1]:
#             return num[i]-1

# def fun(num):
#     i = 1
#     while num[i] - 1 == num[i-1]:
#         i+=1
#     return num[i]-1


# path = 'Lesson_3/task1.txt'
# data = open(path, 'r')
# list = list(data)[0].split(' ')
# data.close
# for i in range(len(list)):
#     list[i] = int(list[i])
# print(list)


# print(fun(list))

path = 'Lesson_3/task1.txt'
data = open(path, 'r')
list = list(data)[0].split(' ')
data.close
for i in range(len(list)):
    list[i] = int(list[i])
print(list)    

res = [(list[i] - 1) for i in range(1,len(list)) if (list[i]-1) != list[i-1]]

print(res)