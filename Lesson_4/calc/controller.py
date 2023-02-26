import model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    operation = view.get_operation() 
    model.init(value_a, value_b)
    if operation == 'sum':
        result = model.sum()
        view.view_data(result)
    elif operation == 'mult':
        result = model.mult()
        view.view_data(result)
    elif operation == 'sub':
        result = model.sub()
        view.view_data(result)
    elif operation == 'div':
        result = model.div()
        view.view_data(result)
    else:
        print('Enter the correct operation (sum, mult, div, sub)')
    
