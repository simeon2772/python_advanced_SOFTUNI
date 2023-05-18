elements = {}

for el in input():
    if el not in elements:
        elements[el] = 0
    elements[el] += 1

for el, times in sorted(elements.items()):
    print(f'{el}: {times} time/s')
    