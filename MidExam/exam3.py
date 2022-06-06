line = input()
chat = list()
while line != 'end':
    line = line.split(' ')
    command = line[0]
    message = line[1]

    if command == 'Chat':
        chat.append(message)
    elif command == 'Delete':
        if message in chat:
            chat.remove(message)
    elif command == 'Edit':
        edited = line[2]
        chat[chat.index(message)] = edited
    elif command == 'Pin':
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif command == 'Spam':
        for m in range(1, len(line)):
            chat.append(line[m])
    line = input()

for m in chat:
    print(''.join(m))
