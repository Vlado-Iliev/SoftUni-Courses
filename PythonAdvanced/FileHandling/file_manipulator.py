from os import remove
from os.path import exists

while True:
    line = input()
    if line == 'End':
        break

    commands = line.split('-')

    if commands[0] == 'Create':
        open(f'./{commands[1]}','w')
    elif commands[0] == 'Add':
        with open(f'./{commands[1]}','a') as file:
            file.write(f'{commands[2]}\n')
    elif commands[0] == 'Replace':
        if not exists(f'./{commands[1]}'):
            print('An error occurred')
            continue

        old_string,new_string = commands[2],commands[3]
        with open(f'./{commands[1]}','r+') as file:
            file_content = file.read().replace(old_string,new_string)
            file.seek(0)
            file.truncate(0)
            file.write(file_content)
    else:
        if not exists(f'./{commands[1]}'):
            print('An error occurred')
            continue
        remove(f'./{commands[1]}')
