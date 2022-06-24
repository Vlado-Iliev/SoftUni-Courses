row, column = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(row)]
best_sum = 0
best_sum_location = []

for i in range(row - 2):
    for j in range(column - 2):
        current_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                          [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                          [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
                          ]
        current_sum = sum([num for sublist in current_matrix for num in sublist])
        if current_sum > best_sum:
            best_sum_location = current_matrix
            best_sum = current_sum
print(f'Sum = {best_sum}')
for r in best_sum_location:
    print(*r, sep=' ')
