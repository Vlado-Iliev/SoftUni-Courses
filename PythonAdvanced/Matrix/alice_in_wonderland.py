size = int(input())
matrix = []
alice_row = 0
alice_col = 0
tb_counter = 0

for row in range(size):
    current_row = input().split()
    for col in range(size):
        if current_row[col] == 'A':
            alice_row = row
            alice_col = col
    matrix.append(current_row)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}


while tb_counter < 10 and 0 <= alice_row < size and 0 <= alice_col < size:
    matrix[alice_row][alice_col] = '*'
    command = input()
    r,c = directions[command](alice_row,alice_col)
    if r < 0 or c < 0 or r >= size or c >= size:
        break
    if matrix[r][c] == 'R':
        matrix[r][c] = '*'
        break
    elif matrix[r][c] != '.' and matrix[r][c] != '*':
        tb_counter += int(matrix[r][c])
        matrix[r][c] = '*'

    alice_row = r
    alice_col = c

if tb_counter < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

for rows in matrix:
    print(*rows,sep=' ')