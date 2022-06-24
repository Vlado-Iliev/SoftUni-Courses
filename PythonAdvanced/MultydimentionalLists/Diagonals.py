rows = int(input())
primary_diagonal = []
secondary_diagonal = []

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

for i in range(rows):
    for j in range(rows):
        if i == j:
            primary_diagonal.append(matrix[i][j])
        if i == rows - j - 1:
            secondary_diagonal.append(matrix[i][j])

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
