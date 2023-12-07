import import_user
import db
import view
def main():
    action = view.choose_action()

    if action == 'Добавить':
        import_user.new_user()
        
    elif action == 'Все':
        print(db.read_user().split('\n'))
    elif action == 'Пользователь':
        search_number = view.enter_user_phonenumber()
        users_list = db.read_user().split('\n')
        users_dict = {}
        for user in users_list:
            user_list = user.split(',')
            try:
                users_dict[user_list[2]] = [user_list[0],user_list[1],user_list[2], user_list[3]]
            except:
                pass
        try:
            print(f'Абонент: {users_dict[search_number]}')
        except:
            print('такого пользователя не существует')

