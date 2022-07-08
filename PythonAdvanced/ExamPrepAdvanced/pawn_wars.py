def find_colour(white, black, size):
    w = None
    b = None

    for row in range(size):
        line = input().split(' ')
        for col in range(len(line)):
            if line[col] == white:
                w = (row, col)
            elif line[col] == black:
                b = (row, col)
    result = (w, b)
    return result


def win_condition(next_row, col, current_player, pawns):
    result = None
    if current_player == 'White':
        if next_row == 0:
            result = 1
        elif pawns['Black'] == (next_row, col + 1) or pawns['Black'] == (next_row, col - 1):
            result = 2
    else:
        if next_row == 7:
            result = 1
        elif pawns['White'] == (next_row, col + 1) or pawns['White'] == (next_row, col - 1):
            result = 2

    return result


def move_pawn(current_player, pawns):
    win = None
    row, col = pawns[current_player]
    if current_player == 'White':
        next_row = row - 1
    else:
        next_row = row + 1
    win = win_condition(next_row, col, current_player, pawns)
    pawns[current_player] = (next_row, col)

    return win


board = []
size = 8

w, b = find_colour('w', 'b', size)
pawns = {
    'White': w,
    'Black': b
}

win = None

current_player, next_player = 'Black', 'White'
while win == None:

    current_player, next_player = next_player, current_player
    win = move_pawn(current_player, pawns)
    if win != None:
        if win == 2:
            row, col = pawns[next_player]
            print(f'Game over! {current_player} win, capture on {chr(col + 97)}{8-row}.')

#            print(f'{current_player}: {chr(col + 97)}{8-row}')
        else:
            row, col = pawns[current_player]
            print(f'Game over! {current_player} pawn is promoted to a queen at {chr(col + 97)}{8 - row}.')

#            print(f'{current_player}: {chr(col + 97)}{8 - row}')
