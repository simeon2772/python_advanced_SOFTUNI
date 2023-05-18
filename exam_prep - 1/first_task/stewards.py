from collections import deque

seat_names = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))

rotations_count = 0
seat_matched = 0
seat_matches_names = []
while rotations_count != 10 and seat_matched != 3:
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    ascii_char = chr(first_number + second_number)
    first_sum_num = str(first_number) + ascii_char
    second_sum_num = str(second_number) + ascii_char
    if first_sum_num in seat_names:
        seat_matched += 1
        seat_matches_names.append(first_sum_num)
    elif second_sum_num in seat_names:
        seat_matched += 1
        seat_matches_names.append(second_sum_num)
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

    rotations_count += 1

print(f'Seat matches: {", ".join(seat_matches_names)}')
print(f'Rotations count: {rotations_count}')