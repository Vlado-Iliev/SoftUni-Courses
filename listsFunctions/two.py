num_of_wagons = int(input())

wagons = [0 for n in range(num_of_wagons)]

command = input()
while command != 'End':
    task = command.split(' ')
    if task[0] == 'add':
        wagons[num_of_wagons - 1] += int(task[1])
    elif task[0] == 'insert':
        wagons[int(task[1])] += int(task[2])
    elif task[0] == 'leave':
        wagons[int(task[1])] -= int(task[2])

    command = input()

print(wagons)