size = int(input())
matrix = [[int(n)for n in input().split()]for _ in range(size)]

command = input().split()

while command[0] != 'END':
    type_command, row, col, number = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
    elif type_command == "Add":
        matrix[row][col] += number
    elif type_command == "Subtract":
        matrix[row][col] -= number

    command = input().split()

[print(*row)for row in matrix]
