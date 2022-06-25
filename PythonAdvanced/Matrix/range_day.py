def is_valid(row, col, matrix, direction, lenght):
    old_row = row
    old_col = col
    flag = False
    for i in range(lenght):
        if direction == 'right':
            col += 1
        if direction == 'left':
            col -= 1
        if direction == 'up':
            row -= 1
        if direction == 'down':
            row += 1

        if row < 0 or col < 0 or row >= 5 or col >= 5:
            flag = True
            break
        elif matrix[row][col] == 'x':
            flag = True
            break

    if not flag:
        return row, col
    else:
        return old_row, old_col


size = 5
shooter_row = 0
shooter_col = 0
matrix = []
shot_targets = []
total_targets = 0

for row in range(5):
    current_row = input().split()
    for col in range(5):
        if current_row[col] == 'A':
            shooter_row = row
            shooter_col = col
        if current_row[col] == 'x':
            total_targets += 1
    matrix.append(current_row)

num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    direction = command[1]
    if command[0] == 'move':
        shooter_row, shooter_col = is_valid(shooter_row, shooter_col, matrix, direction, int(command[2]))
    if command[0] == 'shoot':
        bullet_row = shooter_row
        bullet_col = shooter_col
        for _ in range(5):
            if direction == 'right':
                bullet_col += 1
            if direction == 'left':
                bullet_col -= 1
            if direction == 'up':
                bullet_row -= 1
            if direction == 'down':
                bullet_row += 1

            if 0 > bullet_row or 0 > bullet_col or bullet_row >= 5 or bullet_col >= 5:
                break
            if matrix[bullet_row][bullet_col] == 'x':
                shot_targets.append([bullet_row,bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break
    if len(shot_targets) == total_targets:
        break
if len(shot_targets) < total_targets:
    print(f"Training not completed! {total_targets - len(shot_targets)} targets left.")
else:
    print(f'Training completed! All {total_targets} targets hit.')

print(*shot_targets, sep='\n')
