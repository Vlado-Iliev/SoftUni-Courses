line = input()
command = input()
while command != 'Abracadabra':
    command = command.split(' ')

    if command[0] == 'Abjuration':
        line = line.upper()
        print(line)
    elif command[0] == 'Necromancy':
        line = line.lower()
        print(line)
    elif command[0] == 'Illusion':
        if int(command[1]) < len(line):
            line = line[:int(command[1])] + command[2] + line[int(command[1]) + 1:]
            print('Done!')
        else:
            print("The spell was too weak.")
    elif command[0] == 'Divination':
        if command[1] in line:
            line = line.replace(command[1],command[2])
            print(line)
    elif command[0] == 'Alteration':
        if command[1] in line:
            line = line.replace(command[1],'')
            print(line)
    else:
        print("The spell did not work!")

    command = input()