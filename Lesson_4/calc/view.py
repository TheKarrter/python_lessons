def view_data(data):
    print(f'result = {data}')


def get_value():
    try:
        return int(input('value = '))
    except:
        print('Please, enter integer')
        exit()

def get_operation():
    return (input('operation = '))