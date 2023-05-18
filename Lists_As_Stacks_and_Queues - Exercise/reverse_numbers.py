stack_numbers = input().split()

while stack_numbers:
    reversed_numbers = stack_numbers.pop()
    print(int(reversed_numbers), end=" ")