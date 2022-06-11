num_of_heros = int(input())
game = dict()

for hero in range(num_of_heros):
    new_hero = input().split(' ')
    if new_hero[0] in game.keys():
        game[new_hero[0]] = [int(new_hero[1])+game[new_hero[0]][1],int(new_hero[2])+game[new_hero[0]][2]]
    else:
        game[new_hero[0]] = [int(new_hero[1]), int(new_hero[2])]

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' - ')
    action = command[0]

    if action == 'CastSpell':
        if game[command[1]][1] >= int(command[2]):
            game[command[1]][1] -= int(command[2])
            print(f'{command[1]} has successfully cast {command[3]} and now has {game[command[1]][1]} MP!')
        else:
            print(f'{command[1]} does not have enough MP to cast {command[3]}!')
    elif action == 'TakeDamage':
        if game[command[1]][0] - int(command[2]) > 0:
            game[command[1]][0] -= int(command[2])
            print(f'{command[1]} was hit for {command[2]} HP by {command[3]} and now has {game[command[1]][0]} HP left!')
        else:
            game.pop(command[1])
            print(f'{command[1]} has been killed by {command[3]}!')
    elif action == 'Recharge':
        if game[command[1]][1] + int(command[2]) <= 200:
            game[command[1]][1] += int(command[2])
            print(f'{command[1]} recharged for {command[2]} MP!')
        else:
            recharge = game[command[1]][1] + int(command[2]) - 200
            game[command[1]][1] += recharge
            print(f'{command[1]} recharged for {recharge} MP!')

    elif action == 'Heal':
        if game[command[1]][0] + int(command[2]) <= 100:
            game[command[1]][0] += int(command[2])
            print(f'{command[1]} healed for {command[2]} HP!')
        else:
            recharge = 100 - game[command[1]][0]
            game[command[1]][0] += recharge
            print(f'{command[1]} healed for {recharge} HP!')

for key,value in game.items():
    print(key)
    print(f'  HP: {value[0]}')
    print(f'  MP: {value[1]}')