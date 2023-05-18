def print_func(data):
    if data:
        for car_number in data:
            print(car_number)
    else:
        print("Parking Lot is Empty")


n = int(input())
plate_number = [input() for _ in range(n)]
parking_data = set()

for number in plate_number:
    command, plate = number.split(', ')

    if command == "IN":
        parking_data.add(plate)
    elif command == "OUT":
        parking_data.remove(plate)

print_func(parking_data)