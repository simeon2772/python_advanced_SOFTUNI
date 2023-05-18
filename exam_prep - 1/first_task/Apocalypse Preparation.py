from collections import deque

textiles = deque(int(x) for x in input().split(' '))
medicament = deque(int(x) for x in input().split(' '))

PATCH = 30
BANDAGE = 40
MEDKIT = 100
created_items = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}

while textiles and medicament:
    number = textiles.popleft()
    number2 = medicament.pop()
    total_sum = number + number2
    if total_sum == PATCH:
        created_items['Patch'] += 1
    elif total_sum == BANDAGE:
        created_items['Bandage'] += 1
    elif total_sum == MEDKIT:
        created_items['MedKit'] += 1
    elif total_sum > MEDKIT:
        created_items['MedKit'] += 1
        left_sum = total_sum - MEDKIT
        next_el = medicament.pop()
        finished_cal = next_el + left_sum
        medicament.append(finished_cal)
    else:
        medicament.append(number2 + 10)

if len(textiles) == 0 and len(medicament) == 0:
    print("Textiles and medicaments are both empty.")
elif len(textiles) == 0:
    print("Textiles are empty.")
elif len(medicament) == 0:
    print("Medicaments are empty.")

sorted_dict = sorted(created_items.items(), key=lambda x: (x[1], x[0]), reverse=True)
for item, quantity in sorted_dict:
    print(f'{item} - {quantity}')

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicament)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
