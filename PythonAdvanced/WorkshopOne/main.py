def create_board(x, y):
    game_board = [[0 for column in range(x)] for row in range(y)]
    column_status_list = [(y - 1) for _ in range(x)]

    return game_board, column_status_list


def four_horizontal(player, row, column, board):
    condition = False
    board_column_size = len(board[0])
    counter = 0
    left = column
    while left > 0 and board[row][left] == player:
        left -= 1
    move_right = left
    while move_right < board_column_size and board[row][move_right] == player:
        counter += 1
        move_right += 1

    if counter >= 4:
        condition = True

    return condition


def four_vertical(player, row, column, board):
    board_row_size = len(board)
    condition = False
    counter = 0
    move_down = row
    while move_down < board_row_size and board[move_down][column] == player:
        counter += 1
        move_down += 1

    if counter == 4:
        condition = True

    return condition


def four_main_diagonal(player, row, column, board):
    board_column_size = len(board[0])
    board_row_size = len(board)
    condition = False
    counter = 0
    left_row = row
    left_column = column
    while left_row > 0 and\
            left_column > 0 and\
            board[left_row][left_column] == player:
        left_row -= 1
        left_column -= 1

    right_row = left_row
    right_column = left_column
    while right_row < board_row_size and\
            right_column < board_column_size and\
            board[right_row][right_column] == player:
        counter += 1
        right_row += 1
        right_column += 1

    if counter >= 4:
        condition = True

    return condition


def four_secondary_diagonal(player, row, column, board):
    board_column_size = len(board[0])
    board_row_size = len(board)
    condition = False
    counter = 0
    left_row = row
    left_column = column
    while left_row < board_row_size - 1 and left_column > 0 and board[left_row][left_column] == player:
        left_row += 1
        left_column -= 1

    right_row = left_row
    right_column = left_column
    while right_row > 0 and right_column < board_column_size - 1 and board[right_row][right_column] == player:
        counter += 1
        right_row -= 1
        right_column += 1

    if counter >= 4:
        condition = True

    return condition


def win_check(player, row, column, board):
    condition = any([
        four_horizontal(player, row, column, board),
        four_vertical(player, row, column, board),
        four_main_diagonal(player, row, column, board),
        four_secondary_diagonal(player, row, column, board)
    ])

    return condition


def next_player_turn(current_player, next_player):
    current_player, next_player = next_player, current_player
    column_selected = int(input(f"Player {current_player}, please choose a column")) - 1
    return column_selected, current_player, next_player


def turn_played(player, column_selected, board, column_status):
    board[column_status[column_selected]][column_selected] = player
    column_status[column_selected] -= 1
    win_condition = win_check(player, column_status[column_selected] + 1, column_selected, board)
    print('\n'.join([str(row) for row in board]))

    return win_condition


current_player, next_player = 2, 1
game_over = False
board, column_status = create_board(7, 6)
print('\n'.join([str(row) for row in board]))


while not game_over:

    column_selected, current_player, next_player = next_player_turn(current_player, next_player)
    game_over = turn_played(current_player, column_selected, board, column_status)
    print()
    print('-' * 50)
    print()
    if game_over:

        for _ in range(3):
            print()

        print('* - ' * 20)
        print(f'           Player {current_player} wins !')
        print('* - ' * 20)

        for _ in range(4):
            print()

