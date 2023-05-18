cloths_in_box_stack = list(map(int, input().split(' ')))
capacity_of_rack = int(input())

racks = 1
current_rack_space = capacity_of_rack

while cloths_in_box_stack:
    cloth = cloths_in_box_stack.pop()
    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth
    else:
        racks += 1
        current_rack_space = capacity_of_rack - cloth
print(racks)