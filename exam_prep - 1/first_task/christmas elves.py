from _collections import deque


def elf_no_energy(energy, materials):
    number_of_materials_in_a_box.append(materials)
    energy *= 2
    elf_energy.append(energy)


elf_energy = deque(map(int, input().split()))
number_of_materials_in_a_box = list(map(int, input().split()))
total_elfs_energy = 0
successfully_made_toys = 0
count = 1

while elf_energy and number_of_materials_in_a_box:
    elf = elf_energy.popleft()
    box = number_of_materials_in_a_box.pop()
    if elf < 5:
        number_of_materials_in_a_box.append(box)
        count += 1
        continue

    if count % 3 == 0:
        if elf < box * 2:
            elf_no_energy(elf, box)
            count += 1
            continue
        successfully_made_toys += 2
        total_elfs_energy += box * 2
        elf -= box * 2
        elf += 1
        elf_energy.append(elf)
        count += 1
        continue
    elif count % 5 == 0:
        if count % 3 == 0:
            if elf >= box * 2:
                total_elfs_energy += box * 2
                elf_energy.append(elf)
                count += 1
                continue
            elf_no_energy(elf, box)
            count += 1
            continue
        if elf >= box:
            total_elfs_energy += box
            elf_energy.append(elf)
            count += 1
            continue
        elf_no_energy(elf, box)
        count += 1
        continue
    else:
        if elf >= box:
            successfully_made_toys += 1
            total_elfs_energy += box
            elf -= box
            elf += 1
            elf_energy.append(elf)
            count += 1
            continue
        elf_no_energy(elf, box)
        count += 1


print(f"Toys: {successfully_made_toys}")
print(f"Energy: {total_elfs_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(e) for e in elf_energy)}")
elif number_of_materials_in_a_box:
    print(f"Boxes left: {', '.join(str(b) for b in number_of_materials_in_a_box)}")