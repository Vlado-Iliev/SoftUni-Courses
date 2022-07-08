from collections import deque


def move_rover(direction, rover, board_size):
    row, col = rover

    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    if row < 0:
        row = board_size - 1
    if row > board_size - 1:
        row = 0
    if col < 0:
        col = board_size - 1
    if col > board_size - 1:
        col = 0

    return (row, col)


def check_for_deposit(field, rover):
    row, col = rover
    water = False
    metal = False
    concrete = False
    rock = False
    field_ground = field[row][col]
    if field[row][col] == 'W':
        water = True
        print(f'Water deposit found at ({row}, {col})')

    if field[row][col] == 'M':
        metal = True
        print(f'Metal deposit found at ({row}, {col})')
    if field[row][col] == 'C':
        concrete = True
        print(f'Concrete deposit found at ({row}, {col})')
    if field[row][col] == 'R':
        rock = True
        print(f'Rover got broken at ({row}, {col})')

    return water, metal, concrete, rock


board_size = 6
field = []
rover = ()
for row in range(board_size):
    line = input().split(' ')
    for col in range(len(line)):
        if line[col] == 'E':
            rover = (row, col)
    field.append(line)

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = deque(input().split(', '))

while directions:
    direction = directions.popleft()
    rover = move_rover(direction, rover, board_size)
    water, metal, concrete, rock = check_for_deposit(field, rover)
    if water:
        water_deposit += 1
    if metal:
        metal_deposit += 1
    if concrete:
        concrete_deposit += 1
    if rock:
        break

if water_deposit > 0 and concrete_deposit > 0 and metal_deposit >0:
    print('Area suitable to start the colony.')

else:
    print('Area not suitable to start the colony.')

'''
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right,down, left, left, left
'''
