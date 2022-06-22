n = int(input())

parking_lot = set()

for _ in range(n):
    direction, reg = input().split(', ')
    if direction == 'IN':
        parking_lot.add(reg)
    elif direction == 'OUT':
        parking_lot.remove(reg)

if parking_lot:
    [print(x) for x in parking_lot]

else:
    print(f'Parking Lot is Empty')