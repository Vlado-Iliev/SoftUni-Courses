row, column = [int(x) for x in input().split()]
special_word = input()
matrix = [[None for _ in range(column)] for _ in range(row)]


index = 0
for r in range(row):
    start, stop, step = (0, column, 1) if r % 2 == 0 else (column - 1, -1, -1)
    for i in range(start, stop, step):
        matrix[r][i] = special_word[index]
        index += 1
        if index == len(special_word):
            index = 0

for r in matrix:
    print(*r , sep='')