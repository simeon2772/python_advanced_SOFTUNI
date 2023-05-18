import operator as op


def mathematical_operation(first_number, operator, second_number):
    first_number, second_number = int(first_number), int(second_number)
    valid_operators = {'+': op.add, '-': op.sub, '*': op.mul, '^': op.xor, '/': op.truediv}

    return valid_operators[operator](first_number, second_number)


data = mathematical_operation(*input('Enter: numbers and operator \n').split(' '))
print(data)
