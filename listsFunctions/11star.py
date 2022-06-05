def inventory(startup):
    command = input()
    while command != 'Craft!':
        action = command.split(' - ')
        if action[0] == 'Collect':
            if action[1] in startup:
                continue
            else:
                startup.append(action[1])
        elif action[0] == 'Drop':
            if action[1] in startup:
                startup.remove(action[1])
        elif action[0] == 'Combine Items':
            items = action[1].split(':')
            if items[0] in startup:
                location = startup.index(items[0])
                startup.insert(location + 1, items[1])
        elif action[0] == 'Renew':
            if action[1] in startup:
                startup.remove(action[1])
                startup.append(action[1])
        command = input()

    print(', '.join(startup))


data = input().split(', ')
inventory(data)
