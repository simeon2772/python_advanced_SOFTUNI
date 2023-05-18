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
        [first_sequence.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second_sequence.discard(int(el)) for el in data]
    elif command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)


print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')


