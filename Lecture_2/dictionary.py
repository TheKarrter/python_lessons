dictionary = {} #это пустой словарь
dictionary = \
    {   #ключ слева
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)
print(dictionary['up'])

for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

for v in dictionary:
    print(dictionary[v])

dictionary['up'] = 'up'
print(dictionary)