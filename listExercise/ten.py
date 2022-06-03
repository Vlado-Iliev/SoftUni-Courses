orders = input().split('|')
energy = 100
coins = 100
condition = True

for order in range(len(orders)):
    event = orders[order].split('-')
    name = event[0]
    cost = int(event[1])

    if name == 'rest':
        energy += cost

        if energy > 100:
            over = energy - 100
            gained_energy = cost - over
            energy = 100
        else:
            gained_energy = cost
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif name == 'order':
        if energy >= 30:
            coins += cost
            print(f'You earned {cost} coins.')
            energy -= 30
        else:
            energy += 50
            print('You had to rest!')
    else:
        if cost <= coins:
            coins -= cost
            print(f'You bought {name}.')
        else:
            print(f'Closed! Cannot afford {name}.')
            condition = False
            break

if condition:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')