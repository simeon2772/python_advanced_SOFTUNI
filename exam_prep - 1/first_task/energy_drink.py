from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

MAXIMUM_CAFFEINE_PER_NIGHT = 300
initial_caffeine = 0

while len(energy_drinks) != 0:
    if len(milligrams_of_caffeine) == 0:
        print(f'Drinks left: {", ".join(str(x) for x in energy_drinks) }')
        break

    caffeine = milligrams_of_caffeine.pop()
    energy_drink = energy_drinks.popleft()
    total_caffeine = caffeine * energy_drink

    if initial_caffeine + total_caffeine <= MAXIMUM_CAFFEINE_PER_NIGHT:
        initial_caffeine += total_caffeine
    elif initial_caffeine + total_caffeine > MAXIMUM_CAFFEINE_PER_NIGHT:
        energy_drinks.append(energy_drink)
        if initial_caffeine - 30 > 0:
            initial_caffeine -= 30

if len(energy_drinks) == 0:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f'Stamat is going to sleep with {initial_caffeine} mg caffeine.')