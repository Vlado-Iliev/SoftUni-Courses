gift_list = input().split(' ')
command_lsit = input().split(' ')

while command_lsit[0] != 'No Money':
    if command_lsit[0] == 'OutOfStock':
        while command_lsit[1] in gift_list:
            gift_list.remove(f'{command_lsit[1]}')
    elif command_lsit[0] == 'Required':
        if (len(gift_list)-1) >= int(command_lsit[2]):
            gift_list[int(command_lsit[2])] = f'{command_lsit[1]}'
        else:
            command_lsit = input().split(' ')
            continue
    elif command_lsit[0] == 'JustInCase':
        gift_list[(len(gift_list )- 1)] = f'{command_lsit[1]}'

    command_lsit = input().split(' ')


print(' '.join(gift_list))

