a = (3, 4, 9, 5)
b = (7,)

print(type(a))
print(type(b))


print(a)
print(a[0])
print(a[-1])

print(b)
print(b[0])

for item in a:
    print(item)

t = tuple(['red', 'green', 'blue'])  #по сути конфертируем список в кортеж
red, green, blue = t 
print('r: {} g: {} b: {}'.format(red,green,blue)) #еще один формат вывода