rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    line = input().split()
    if line[0] == 'END':
        break
    command = line[0]
    row, col, value = int(line[1]), int(line[2]), int(line[3])
    if 0 <= row < rows and 0 <= col < rows:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for r in matrix:
    print(*r, sep=' ')