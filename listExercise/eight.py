fire_cells = input().split('#')
water_value = int(input())
effort = 0
total_fire = 0
condition = False
print('Cells:')

for fire in range(len(fire_cells)):
    current = fire_cells[fire].split(' = ')
    if current[0] == 'High':
        if 81 <= int(current[1]) <= 125 and int(current[1]) <= water_value:
            condition = True
    elif current[0] == 'Medium' and int(current[1]) <= water_value:
        if 51 <= int(current[1]) <= 80:
            condition = True
    elif current[0] == 'Low' and int(current[1]) <= water_value:
        if 1 <= int(current[1]) <= 50:
            condition = True

    if condition:
        water_value -= int(current[1])
        total_fire += int(current[1])
        print(f'- {current[1]}')
        effort += int(current[1]) * 0.25
        condition = False

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
