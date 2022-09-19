day_of_week = int(input("Проверь,является ли день выходным \nВведите номер дня: "))
def check_day(num_day):
    match num_day:
        case 1 :
            print("Нет")
        case 2 :
            print("Нет")
        case 3 :
            print("Нет")
        case 4 :
            print("Нет")
        case 5 :
            print("Нет")
        case 6 :
            print("Да")
        case 7 :
            print("Да")
        case default :
            print("Неверный номер дня")    

    
check_day(day_of_week)
