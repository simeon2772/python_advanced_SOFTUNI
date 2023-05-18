from _collections import deque

name_of_players = input().split(" ")
steps_of_hot_potato = int(input())

players_queue = deque(name_of_players)
counter = 0

while len(players_queue) > 1:
    counter += 1
    current_name_of_player = players_queue.popleft()

    if counter == steps_of_hot_potato:
        print(f"Removed {current_name_of_player}")
        counter = 0
    else:
        players_queue.append(current_name_of_player)

print(f"Last is {players_queue[0]}")
first_sequence = {int(num) for num in input().split()}
second_sequence = {int(num) for num in input().split()}

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)
    if command == "Add First":
        [first_sequence.add(int(el)) for el in data]
    elif command == "Add Second":
        [second_sequence.add(int(el)) for el in data]
    elif command == "Remove First":
        [first_sequence.remove(int(el)) for el in data]
    elif command == "Remove Second":
        [second_sequence.remove(int(el)) for el in data]
    elif command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(", ".join(sorted(first_sequence)))
print(", ".join(sorted(second_sequence)))


