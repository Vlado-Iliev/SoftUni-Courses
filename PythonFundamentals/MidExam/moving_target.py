targets = input().split(' ')
targets = list(map(int, targets))
command = input()

while command != 'End':
    command = command.split(' ')
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == 'Shoot' and 0 <= index < len(targets):
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif action == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif action == 'Strike':
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print('Strike missed!')
    command = input()

targets = list(map(str, targets))
print('|'.join(targets))
