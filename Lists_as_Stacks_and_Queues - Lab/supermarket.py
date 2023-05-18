from _collections import deque

people_line = deque()
COMMAND_END = "End"
COMMAND_PAID = "Paid"

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{len(people_line)} people remaining.")
        break
    elif command == COMMAND_PAID:
        while people_line:
            print(people_line.popleft())
    else:
        people_line.append(command)