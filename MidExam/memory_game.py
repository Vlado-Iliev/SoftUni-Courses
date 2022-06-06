table = input().split(' ')
command = input()
moves_counter = 0
while command != 'end':
    moves_counter += 1
    indexes = command.split(' ')
    index_one, index_two = int(indexes[0]), int(indexes[1])
    if index_one == index_two or index_one < 0 or index_two < 0:
        #print(f"-{moves_counter}a")
        table.insert(int(len(table)/2), f"-{moves_counter}a")
        table.insert(int(len(table) / 2), f"-{moves_counter}a")
        print('Invalid input! Adding additional elements to the board')
    else:
        if table[index_one] == table[index_two]:
            wanted = table[index_one]
            print(f"Congrats! You have found matching elements - {table[index_one]}!")
            while wanted in table:
                table.remove(wanted)

        else:
            print('Try again!')
    if len(table) == 0:
        print(f'You have won in {moves_counter} turns!')
        break
    command = str(input())

if len(table) > 0:
    print('Sorry you lose :(')
    print(' '.join(table))
