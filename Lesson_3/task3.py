# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв"

my_string = 'Мы неабв очень любим Питон иабв Джавуабв!'
my_filter = 'абв'

print(' '.join(filter(lambda x: not my_filter in x, my_string.split())))

my_list = my_string.split()

res = [my_list[i] for i in range(len(my_list)) if my_filter not in my_list[i]]

print(res)

print(' '.join([my_list[i] for i in range(len(my_list)) if my_filter not in my_list[i]]))

print(' '.join(res))