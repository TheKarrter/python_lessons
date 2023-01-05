# В ФАЙЛЕ находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнить условие A[i] - 1 = A[i-1]
# Найдите это число
def fun(num):
    for i in range(1,len(num)):
        if num[i] - 1 != num[i-1]:
            return num[i]-1


path = 'Lesson_3/task1.txt'
data = open(path, 'r')
list = list(data)[0].split(' ')
data.close
for i in range(0, len(list)):
    list[i] = int(list[i])
print(list)



print(fun(list))
    