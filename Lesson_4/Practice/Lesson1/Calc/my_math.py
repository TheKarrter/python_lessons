def equation(operation: str):
    if operation == '+':
        return lambda a,b: a + b
    elif operation == '-':
        return lambda a,b: a - b
    elif operation == '*':
        return lambda a,b: a * b
    elif operation == '/':
        return lambda a,b: a / b
    elif operation == '//':
        return lambda a,b: a // b
    elif operation == '%':
        return lambda a,b: a % b
    elif operation == '**':
        return lambda a,b: a**b  