#2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

N = 30
list = []
k = 0
for i in range(2, N+1):
    if N%i == 0:
        for j in range(2, i//2 + 1):
            if i%j == 0: k+=1
        if k == 0:
            list.append(i)
        else: k = 0

print(list)