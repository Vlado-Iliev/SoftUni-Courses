def player_switch(current_player, next_player, board):
    current_player, next_player = next_player, current_player
    while True:
        index = input(f'{current_player[0]} choose a free position[1-9]: ')
        if index.isdigit() and board[(int(index) - 1) // len(board)][(int(index) + 2) % len(board)] == ' ':
            index = int(index)
            break
    board[(index - 1) // len(board)][(index + 2) % len(board)] = current_player[1]

    for i in range(len(board) - 1, -1, -1):
        print('|  '.join([f'{str(x)}  ' for x in board[i]]))

    return current_player, next_player


def horizontal_win(board, player):
    win = False

    wanted_symbol = player[1]
    for row in range(len(board)):
        counter = 0
        for i in range(len(board)):
            if board[row][i] == wanted_symbol:
                counter += 1
        if counter == 3:
            win = True
    return win


def vertical_win(board, player):
    win = False
    wanted_symbol = player[1]
    for i in range(len(board)):
        counter = 0
        for row in range(len(board)):
            if board[row][i] == wanted_symbol:
                counter += 1
        if counter == 3:
            win = True
    return win


def primary_diagonal_win(board, player):
    win = False
    wanted_symbol = player[1]
    counter = 0
    for x in range(len(board)):
        if board[x][x] == wanted_symbol:
            counter += 1
    if counter == 3:
        win = True
    return win


def secondary_diagonal_win(board, player):
    win = False
    wanted_symbol = player[1]
    counter = 0
    for x in range(len(board)):
        if board[x][len(board) - x - 1] == wanted_symbol:
            counter += 1
    if counter == 3:
        win = True
    return win


def draw(board):
    condition = True
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == ' ':
                condition = False
    if condition:
        for _ in range(3):
            print()
        print('* - ' * 6)
        print(f'-       Draw         *')
        print('* - ' * 6)
        for _ in range(3):
            print()

    return condition


def check_for_winner(board, player):
    condition = False
    if any(
            [horizontal_win(board, player),
             vertical_win(board, player),
             primary_diagonal_win(board, player),
             secondary_diagonal_win(board, player),
             ]
    ):
        condition = True

    return condition


def play_the_game(player_one, player_two):
    board_size = 3
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    while True:
        player_two, player_one = player_switch(player_two, player_one, board)
        if draw(board):
            break
        if check_for_winner(board, player_two):
            for _ in range(3):
                print()
            print('* - ' * 6)
            print(f'-       {player_two[0]} won !         *')
            print('* - ' * 6)
            for _ in range(3):
                print()
            break


def player_assigment():
    player_one_name = input('Player one please choose name: ')
    player_two_name = input('Player two please choose name: ')
    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O' ").upper()
        if player_one_symbol == 'X' or player_one_symbol == 'O':
            break

    player_one = (player_one_name, player_one_symbol)
    player_two = (player_two_name, 'O' if player_one_symbol == 'X' else 'X')

    print('|  7  |  8  |  9  |')
    print('|  4  |  5  |  6  |')
    print('|  1  |  2  |  3  |')

    print(f'{player_one_name} starts first !')
    return player_one, player_two


player_one, player_two = player_assigment()
play_the_game(player_one, player_two)
