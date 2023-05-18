def operate(operator, *numbers):
    if operator == '+':
        result = 0
        for num in numbers:
            result += num
        return result
    elif operator == '-':
        result = 0
        for num in numbers:
            result -= num
        return result
    elif operator == '*':
        result1 = 1
        for num in numbers:
            result1 *= num
        return result1
    elif operator == '/':
        result1 = 1
        for num in numbers:
            result1 /= num
        return result1


print(operate("-", 5, 2))