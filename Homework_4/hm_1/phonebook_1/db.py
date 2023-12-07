def save_user(name, second_name, phonenumber, discription):
    path = 'урок 1/Homework_4/hm_1/phonebook_1/db.txt'
    with open(path, 'a') as file:
        file.write(f'{name},{second_name},{phonenumber},{discription}\n')

def read_user():
    path = 'урок 1/Homework_4/hm_1/phonebook_1/db.txt'
    with open(path, 'r') as file:
        return file.read()