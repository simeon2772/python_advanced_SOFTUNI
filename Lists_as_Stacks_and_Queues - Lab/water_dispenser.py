from _collections import deque


def add_names_to_queue():
    people = deque()
    while True:
        names_of_people = input()
        if names_of_people == COMMAND_START:
            break
        people.append(names_of_people)
    return people


COMMAND_START = "Start"
COMMAND_END = "End"
COMMAND_REFILL = "refill"
water_in_dispenser = int(input())
people_in_queue = add_names_to_queue()

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{water_in_dispenser} liters left")
        break
    elif command.startswith(COMMAND_REFILL):
        refill_liters_data = command.split(" ")
        refill_liters = int(refill_liters_data[1])
        water_in_dispenser += refill_liters
    else:
        liters_needed = int(command)
        if liters_needed <= water_in_dispenser:
            print(f"{people_in_queue.popleft()} got water")
            water_in_dispenser -= liters_needed
        else:
            print(f"{people_in_queue.popleft()} must wait")

