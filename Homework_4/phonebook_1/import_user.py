import view
import db

def new_user():
    user_name = view.enter_user_name()
    user_second_name = view.enter_user_second_name()
    user_phonenumber = view.enter_user_phonenumber()
    user_disctiption = view.enter_user_disctiption()
    db.save_user(user_name,user_second_name,user_phonenumber,user_disctiption)

