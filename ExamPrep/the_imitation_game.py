line = input()
command = input()

while command != 'Decode':
    instructuons = command.split('|')

    if instructuons[0] == 'Move':
        front = line[:int(instructuons[1])]
        back = line[int(instructuons[1]):]
        line = back + front
    elif instructuons[0] == 'Insert':
        front = line[:int(instructuons[1])]
        back = line[int(instructuons[1]):]
        line = front + instructuons[2] + back
    elif instructuons[0] == 'ChangeAll':
        line = line.replace(instructuons[1],instructuons[2])


    command = input()

print(f'The decrypted message is: {line}')