def next_step(row, col, direction):
    santa_row = row
    santa_col = col
    if direction == 'right':
        santa_col += 1
    if direction == 'left':
        santa_col -= 1
    if direction == 'up':
        santa_row -= 1
    if direction == 'down':
        santa_row += 1

    return [santa_row, santa_col]


def cookie_found(row, col, matrix):
    for_present = []
    possible = [
        [row + 1, col],
        [row - 1, col],
        [row, col + 1],
        [row, col - 1]
    ]
    for house in possible:
        a = house[0]
        b = house[1]
        if 0 <= a < len(matrix) and 0 <= b < len(matrix):
            if matrix[a][b] == 'V' or matrix[a][b] == 'X':
                for_present.append([a, b])
    return for_present


number_of_presents = int(input())
size = int(input())
total_nice_kids = 0
total_presents = number_of_presents
santa_row = 0
santa_col = 0
matrix = []
nice_kids_presents = 0
for row in range(size):
    current_row = input().split()
    for col in range(size):
        if current_row[col] == 'S':
            santa_row = row
            santa_col = col
        if current_row[col] == 'V':
            total_nice_kids += 1

    matrix.append(current_row)

while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa_row][santa_col] = '-'

    next_row, next_col = next_step(santa_row, santa_col, command)
    if matrix[next_row][next_col] == 'X':
        matrix[next_row][next_col] = '-'
    if matrix[next_row][next_col] == 'V':
        matrix[next_row][next_col] = '-'
        nice_kids_presents += 1
        number_of_presents -= 1
    if matrix[next_row][next_col] == 'C':
        kids_for_presents = cookie_found(next_row, next_col, matrix)
        for house in kids_for_presents:
            if matrix[house[0]][house[1]] == 'V':
                nice_kids_presents += 1

            number_of_presents -= 1
            matrix[house[0]][house[1]] = '-'

    matrix[next_row][next_col] = 'S'
    if number_of_presents <= 0:
        break
    santa_row = next_row
    santa_col = next_col

if number_of_presents <= 0 and total_nice_kids > nice_kids_presents:
    print('Santa ran out of presents!')

for r in matrix:
    print(*r, sep=' ')

if total_nice_kids > nice_kids_presents:
    print(f'No presents for {total_nice_kids - nice_kids_presents} nice kid/s.')
else:
    print(f'Good job, Santa! {nice_kids_presents} happy nice kid/s.')
