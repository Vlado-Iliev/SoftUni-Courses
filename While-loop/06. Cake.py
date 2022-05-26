cake_length = int(input())
cake_width = int(input())
available_pieces = cake_width * cake_length
pieces_counter = available_pieces
command = input()
while command != 'STOP':
    pieces_counter -= int(command)
    if pieces_counter <= 0:
        break
    command = input()

if pieces_counter < 0:
    print(f'No more cake left! You need {abs(pieces_counter)} pieces more.')
else:
    print(f'{pieces_counter} pieces are left.')