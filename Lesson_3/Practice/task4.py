# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /,* приоритет операций сстандартный.
import re


string = '2 + 3 * 5'

operation = ''.join(string.split())
operators = []

print(string)
print(re.split('[+*/-]', string))

for i in operation:
    if i in '-+*/':
        operators.append(i)

print(operators)