world = dict()
command = input()
while command != 'Sail':
    command = command.split('||')
    town = command[0]
    population = int(command[1])
    gold = int(command[2])
    if town in world:
        world[town][0] += population
        world[town][1] += gold
    else:
        world[town] = [population, gold]

    command = input()

while True:
    line = input()
    if line == 'End':
        break

    line = line.split('=>')
    action = line[0]
    town = line[1]
    if action == 'Plunder':
        people = int(line[2])
        gold = int(line[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        world[town][0] -= people
        world[town][1] -= gold
        if world[town][0] <= 0 or world[town][1] <= 0:
            print(f'{town} has been wiped off the map!')
            world.pop(town)
    elif action == 'Prosper':
        gold = int(line[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
            continue
        else:
            world[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {world[town][1]} gold.')

if len(world) > 0:
    print(f'Ahoy, Captain! There are {len(world)} wealthy settlements to go to:')
    for key,value in world.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')

