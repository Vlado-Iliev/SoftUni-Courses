def shootin_range(target):
    target_value = list(map(int, target))
    command = input()
    while command != 'End':
        operations = command.split(' ')
        if operations[0] == 'Shoot':
            if int(operations[1]) < len(target_value):
                target_value[int(operations[1])] -= int(operations[2])
                if target_value[int(operations[1])] <= 0:
                    target_value.pop(int(operations[1]))

        elif operations[0] == 'Add':
            if int(operations[1]) < len(target):
                target_value.insert(int(operations[1]), int(operations[2]))
            else:
                print('Invalid placement!')

        elif operations[0] == 'Strike':
            a = int(operations[1]) + int(operations[2])
            b = int(operations[1]) - int(operations[2])
            if a < len(target) and b >= 0:
                for i in range(b, a):
                    target_value.pop(i)
            else:
                print('Strike missed!')
        command = input()

    target_str = list(map(str, target_value))
    print('|'.join(target_str))


targets = input().split(' ')
shootin_range(targets)
