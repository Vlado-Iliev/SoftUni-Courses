def valentine(houses):
    neighborhood = list(map(int, houses))
    command = input()
    current_position = 0
    condition = True
    while command != 'Love!':
        operation = command.split(' ')
        current_position += int(operation[1])
        if current_position > len(neighborhood) - 1:
            current_position = 0
        if neighborhood[current_position] > 0:
            neighborhood[current_position] -= 2
            if neighborhood[current_position] <= 0:
                print(f"Place {current_position} has Valentine's day.")
                neighborhood[current_position] = 0
        else:
            print(f"Place {current_position} already had Valentine's day.")
        command = input()
    print(f"Cupid's last position was {current_position}.")
    counter = 0
    for h in range(len(neighborhood)):
        if neighborhood[h] != 0:
            counter += 1
            condition = False
    if condition:
        print(f'Mission was successful.')
    else:
        print(f'Cupid has failed {counter} places.')


neighborhood = input().split('@')
valentine(neighborhood)
