def save_number(number_1, number_2, operation):
    path = 'Lesson_4/Practice/Lesson1/Calc/db.txt'
    with open(path, 'a') as file:
        file.write(f'{number_1} {operation} {number_2}\n')

def read_number():
    path = 'Lesson_4/Practice/Lesson1/Calc/db.txt'
    with open(path, 'r') as file:
         return file.read()