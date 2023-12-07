#4) Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = 4
polynomial = ''

for i in range(-k, -1):
    polynomial = polynomial + str(random.randint(0,100))+'x^'+str(-i) + '+'
polynomial += str(random.randint(0,100))+'x'+'+'
polynomial += str(random.randint(0,100))

print(polynomial)