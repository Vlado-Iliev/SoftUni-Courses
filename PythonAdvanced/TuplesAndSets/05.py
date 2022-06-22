n = int(input())

vip_guests = set()
regular_guests = set()
for _ in range(n):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

while True:
    command = input()
    if command == 'END':
        break
    if command in vip_guests:
        vip_guests.remove(command)
    else:
        regular_guests.remove(command)

print(len(vip_guests|regular_guests))
[print(x) for x in (sorted(vip_guests) + sorted(regular_guests))]
