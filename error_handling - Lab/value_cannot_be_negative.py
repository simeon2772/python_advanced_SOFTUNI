class ValueCannotBeNegative(Exception):
    pass


numbers = [int(input()) for _ in range(5)]

for num in numbers:
    if num < 0:
        raise ValueCannotBeNegative("Value cannot be negative")
