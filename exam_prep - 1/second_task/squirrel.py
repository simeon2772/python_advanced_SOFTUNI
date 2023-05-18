hazel_nuts = 0
size = int(input())
directions_commands = input().split(", ")


def get_direction(directions, index):
    return directions[index % len(directions)]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
player_pos = []

for row in range(size):
    line = list(input())
    matrix.append(line)

    if "s" in line:
        player_pos = [row, line.index("s")]

index = 0
end_game = False
while True:

    r = player_pos[0] + directions[get_direction(directions_commands, index)][0]
    c = player_pos[1] + directions[get_direction(directions_commands, index)][1]
    index += 1

    if not (0 <= r < size and 0 <= c < size):
        print("The squirrel is out of the field.")
        end_game = True
        break
    player_pos = [r, c]

    if matrix[r][c] == "h":
        hazel_nuts += 1
        matrix[r][c] = '*'

    if hazel_nuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

    if matrix[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        end_game = True
        break

if hazel_nuts < 3 and not end_game:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazel_nuts}")
