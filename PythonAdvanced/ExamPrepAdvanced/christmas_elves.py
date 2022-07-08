from collections import deque

elves = deque(input().split())
boxes = input().split()

total_toys_made = 0
total_energy_used = 0
elf_count = 1

while elves and boxes:
    elf = int(elves.popleft())
    if elf < 5:
        continue
    box = int(boxes.pop())
    toys_made = 0
    energy_used = 0
    third = False
    fifth = False
    condition = False
    second_condition = False

    if elf_count % 3 == 0:
        third = True
    if elf_count % 5 == 0:
        fifth = True

    if elf >= box:
        if third:
            if elf >= box * 2:
                toys_made = 2
                energy_used = box * 2
                condition = True
            else:
                elf *= 2
                elves.append(elf)
                boxes.append(box)
                elf_count += 1

                continue
        if fifth:
            second_condition = True

        if condition:
            total_toys_made += toys_made
            total_energy_used += energy_used
            elves.append(elf - (energy_used - 1))
            elf_count += 1
            condition = False
            continue

        else:
            elf -= box - 1
            if not second_condition:
                toys_made += 1
            energy_used = box

    else:
        elf *= 2
        elves.append(elf)
        elf_count += 1
        boxes.append(box)
        continue

    total_toys_made += toys_made
    total_energy_used += energy_used
    elves.append(elf)
    elf_count += 1

print(f'Toys: {total_toys_made}')
print(f'Energy: {total_energy_used}')
if elves:
    print(f'Elves left: {", ".join([str(x) for x in elves])}')
if boxes:
    print(f'Boxes left: {", ".join([str(x) for x in boxes])}')
