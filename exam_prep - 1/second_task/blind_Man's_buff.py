size_N, size_M = [int(x) for x in input().split()]

touched_opponents = 0
moves_made = 0

matrix = []
player_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size_N):
    line = list(input().split(' '))
    matrix.append(line)

    if "B" in line:
        player_pos = [row, line.index("B")]

while True:
    command = input()
    if command == "Finish":
        break

    row = player_pos[0] + directions[command][0]
    col = player_pos[1] + directions[command][1]

    if not (0 <= row < size_N and 0 <= col < size_M):
        continue
    player_pos = [row, col]

    if matrix[row][col] == "O":
        continue
    elif matrix[row][col] == "-":
        moves_made += 1
    elif matrix[row][col] == "P":
        touched_opponents += 1
        moves_made += 1
        matrix[row][col] = '-'

    if touched_opponents == 3:
        break


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")