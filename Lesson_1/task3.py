# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# "Я люблю питон!"
# "лю" -> 2
# 
# # print(str.count(str_find, 0, len(str)))



# i = 0
# for i in len(str):
#     if str[i] + str[i+1] == str_find

str = input("Введите строку: ")
str1 = input("Введите подстроку: ")
str2 = ""
j = 0
count = 0
while (count < len(str)-len(str1)+1):
    for i in range (len(str1)):
        str2 += str[count+i]
    if (str1 == str2):
        j+=1
    count+=1
    str2 = ""
print (j)


# str1 = input('Введите строку 1: ')
# str2 = input('Введите строку 2: ')

# print(len(str1.split(str2)) - 1)
