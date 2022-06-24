rows = int(input())
primary_diagonal = []
secondary_diagonal = []

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for i in range(rows):
    for j in range(rows):
        if i == j:
            primary_diagonal.append(matrix[i][j])
        if i == rows - j - 1:
            secondary_diagonal.append(matrix[i][j])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))