import view
import db
import my_math

def process_calc():
    number_1 = view.request_number()
    number_2 = view.request_number()
    operation = view.request_operation()
    db.save_number(number_1, number_2, operation)
    # print(my_math.equation(operation)(number_1, number_2))
    result = my_math.equation(db.read_number().split()[-2])(int(db.read_number().split()[-3]),int(db.read_number().split()[-1]))
    view.output(result)
