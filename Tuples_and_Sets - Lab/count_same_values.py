values = tuple(map(float, input().split()))
my_values_dict = {}

for value in values:
    if value not in my_values_dict:
        my_values_dict[value] = 0
    my_values_dict[value] += 1

for k, v in my_values_dict.items():
    print(f"{k} - {v} times")