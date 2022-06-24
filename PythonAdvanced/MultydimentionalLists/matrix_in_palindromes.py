def command_validator(commands, rows, columns):
    if commands[0] == 'swap' and len(commands) == 5 and \
            0 <= int(command[1]) < rows and 0 <= int(command[2]) < columns and \
            0 <= int(command[3]) < rows and 0 <= int(command[4]) < columns:
        return True
    else:
        return False


row, column = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(row)]

while True:
    line = input()
    if line == 'END':
        break
    command = line.split()
    if command_validator(command, row, column):
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = \
            matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
    else:
        print(f'Invalid input!')
        continue

    for r in matrix:
        print(*r, sep=' ')

