from collections import deque

programmers_time = deque(map(int, input().split()))
number_of_tasks = list(map(int, input().split()))

ducks_info = {"Darth Vader Ducky": [0, 60],
              "Thor Ducky": [61, 120],
              "Big Blue Rubber Ducky": [121, 180],
              "Small Yellow Rubber Ducky": [181, 240]}

given_ducks = {"Darth Vader Ducky": 0,
               "Thor Ducky": 0,
               "Big Blue Rubber Ducky": 0,
               "Small Yellow Rubber Ducky": 0}

while programmers_time and number_of_tasks:
    prog_time = programmers_time.popleft()
    task = number_of_tasks.pop()
    total = prog_time * task

    for duck_name, quantity in ducks_info.items():
        if quantity[0] <= total <= quantity[1]:
            given_ducks[duck_name] += 1
            break
        elif total > ducks_info["Small Yellow Rubber Ducky"][1]:
            programmers_time.append(prog_time)
            task -= 2
            number_of_tasks.append(task)
            break


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in given_ducks.items():
    print(f"{key}: {value}")
