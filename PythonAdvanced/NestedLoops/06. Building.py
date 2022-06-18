flat_floors = int(input())
rooms_per_floor = int(input())

for f in range(flat_floors, 0, -1):
    for a in range(0, rooms_per_floor):
        if f == flat_floors :
            print(f'L{f}{a}', end=" ")

        elif f % 2 == 0 :
            print(f'O{f}{a}', end=" ")

        else:
            print(f'A{f}{a}', end=" ")
    print()