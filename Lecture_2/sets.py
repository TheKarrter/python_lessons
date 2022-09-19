colors = {'red', 'green', 'blue'}

print(type(colors))

print(colors)
colors.add('red')
print(colors)
colors.add('grey')
print(colors)
colors.remove('red')
print(colors)
colors.discard('red') #если есть - удалит, если нет - то ничего не произойдет и ошибку не выдаст
print(colors)
colors.clear()
print(colors)

a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy()
print(c)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
dl = a.difference(b)
print(dl)
dr = b.difference(a)
print(dr)


s = frozenset(a) #неизменяемое множество
