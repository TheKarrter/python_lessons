#4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = 25
bin_num_str = ''

while num > 0:
    bin_num_str += str(num%2)
    num //= 2

for i in reversed(bin_num_str):
    print(i, end = '')