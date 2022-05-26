width_of_free_space = int(input())
lenght_of_free_space = int(input())
height_of_free_space = int(input())
free_space = width_of_free_space * lenght_of_free_space * height_of_free_space
box_space = 0

command = input()

while command != 'Done' :
    boxes = int(command)
    box_space += boxes
    if free_space > box_space:
        command = input()
    else:
        break

if box_space <= free_space :
    space_left = free_space - box_space
    print(f'{space_left} Cubic meters left.')
else:
    space_needed = box_space - free_space
    print(f'No more free space! You need {space_needed} Cubic meters more.')