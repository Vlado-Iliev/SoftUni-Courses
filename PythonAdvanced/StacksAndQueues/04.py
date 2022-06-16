from collections import deque

line = deque()
dispenser = int(input())
condition = False
while True:
    command = input()

    if command == 'Start':
        condition = True
        break
    else:
        line.append(command)

if condition:
    while True:
        command = input()
        if command == 'End':
            print(f'{dispenser} liters left')
            break
        elif command.startswith('refill '):
            command = command.split(' ')
            refill = int(command[1])
            dispenser += refill
        else:
            wanted = int(command)
            if wanted <= dispenser:
                dispenser -= wanted
                name = line.popleft()
                print(f'{name} got water')
            else:
                name = line.popleft()
                print(f'{name} must wait')


