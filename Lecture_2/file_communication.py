# colors = ['red', 'green', 'blue']
# data = open('Lecture_2/file.txt', 'a')
# data.writelines(colors) #без разделителей
# data.close()

# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

path = 'Lecture_2/file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
