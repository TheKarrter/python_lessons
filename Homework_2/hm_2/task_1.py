#1) Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141
import math

n = math.pi
d = 0.00001

print(round(n, len(str(d).split('.')[-1])))