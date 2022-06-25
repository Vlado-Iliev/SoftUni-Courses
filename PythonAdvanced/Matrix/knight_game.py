def horse_play(row, col, matrix):
    possible_moves = [
         [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col + 2],
        [row - 1, col - 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
        [row + 1, col + 2],
        [row + 1, col - 2]
    ]
    counter = 0
    for move in possible_moves:
        if 0 <= move[0] < len(matrix) and 0 <= move[1] < len(matrix):
            if matrix[move[0]][move[1]] == 'K':
                counter += 1
    return counter


n = int(input())
matrix = []
counter = 0
best_score = 0
best_row = None
best_col = None

for row in range(n):
    current_row = input()
    r = []
    for col in range(n):
        r.append(current_row[col])
    matrix.append(r)

while True:
    best_score = 0
    for rows in range(n):
        for cols in range(n):
            if matrix[rows][cols] == '0':
                continue
            current_counter = horse_play(rows, cols, matrix)
            if current_counter > best_score:
                best_row = rows
                best_col = cols
                best_score = current_counter
    if best_score == 0 or matrix[best_row][best_col] != 'K':
        break
    matrix[best_row][best_col] = '0'
    counter += 1

print(counter)
