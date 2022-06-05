def chair_sorter(num_of_rooms):
    free_chair_counter = 0
    condition = True
    for room in range(1,num_of_rooms + 1):
        data = input().split(' ')
        diff = abs(len(data[0]) - int(data[1]))
        if len(data[0]) < int(data[1]):
            print(f'{diff} more chairs needed in room {room}')
            condition = False
        else:
            free_chair_counter += diff

    if condition:
        print(f'Game On, {free_chair_counter} free chairs left')


number_of_rooms = int(input())
chair_sorter(number_of_rooms)