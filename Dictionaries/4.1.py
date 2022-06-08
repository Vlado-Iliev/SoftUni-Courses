def reader(line,phonebook):
    for person in range(int(line)):
        name = input()
        if name in phonebook.keys():
            print(f'{name} -> {phonebook[name]}')
        else:
            print(f'Contact {name} does not exist.')


phonebook = dict()

while True:
    line = input()
    if len(line) == 1:
        reader(line,phonebook)
        break
    contact = line.split('-')
    if contact[0] not in phonebook.keys():
        phonebook[contact[0]] = contact[1]
    else:
        phonebook[contact[0]] = contact[1]

