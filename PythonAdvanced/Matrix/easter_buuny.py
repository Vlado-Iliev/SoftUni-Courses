size = int(input())
matrix = []


bunny_row = None
bunny_col = None

for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(size):
        if current_row[col] == 'B':
            bunny_row = row
            bunny_col = col


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}


best_score = float('-inf')
best_direction = ''
best_path = []


for direction in directions:
    current_sum = 0
    rows, cols = directions[direction](bunny_row,bunny_col)
    current_path = []
    while 0 <= rows< size and 0 <= cols < size and matrix[rows][cols] != 'X':
        current_sum += int(matrix[rows][cols])
        current_path.append([rows,cols])
        rows, cols = directions[direction](rows, cols)

    if current_sum > best_score:
        best_score = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path,sep='\n')
print(best_score)
