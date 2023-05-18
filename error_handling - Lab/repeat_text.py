def some_func(some_text, num):
    return some_text * num


try:
    text = input()
    numbers = int(input())
    print(some_func(text, numbers,))

except ValueError:
    print('Variable times must be an integer')
