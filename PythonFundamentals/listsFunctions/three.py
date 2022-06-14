todo = ['' for i in range(10)]
command = input()
new_todo = list()

while command != 'End':
    task = command.split('-')
    todo[int(task[0]) - 1] = task[1]

    command = input()

new_todo = list(filter(lambda x: x != '',todo))
print(new_todo)