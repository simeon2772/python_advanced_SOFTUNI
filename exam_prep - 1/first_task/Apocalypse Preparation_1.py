from _collections import deque


def create_obj_in_dict(obj, dict):
    if obj not in dict:
        dict[obj] = 1
    else:
        dict[obj] += 1


textiles = deque(map(int, input().split()))
medicament = list(map(int, input().split()))

items_info = {"Patch": 30, "Bandage": 40, "MedKit": 100}
created_items = {}
created = False
mat_over = False
med_over = False
both_over = False

while True:
    if not textiles and not medicament:
        both_over = True
        break
    elif not textiles:
        mat_over = True
        break
    elif not medicament:
        med_over = True
        break

    mat = textiles.popleft()
    med = medicament.pop()
    total = mat + med

    for item, quantity in items_info.items():
        if total == quantity:
            create_obj_in_dict(item, created_items)
            created = True
    if total > items_info["MedKit"]:
        if created_items["MedKit"]:
            created_items["MedKit"] += 1
        med = medicament.pop()
        med += total - items_info["MedKit"]
        medicament.append(med)
        created = True

    if not created:
        med += 10
        medicament.append(med)

    created = False

if both_over:
    print("Textiles and medicaments are both empty.")
elif mat_over:
    print("Textiles are empty.")
elif med_over:
    print("Medicaments are empty.")

for item, amount in sorted(created_items.items(), key=lambda v: (-v[1], v[0])):
    print(f"{item} - {amount}")

if textiles:
    print(f"Textiles left: {', '.join(str(t) for t in textiles)}")
if medicament:
    print(f"Medicaments left: {', '.join(str(m) for m in reversed(medicament))}")