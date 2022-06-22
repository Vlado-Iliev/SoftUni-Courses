from collections import deque

material_boxes = [int(x) for x in (input().split())]
magic_values = deque([int(x) for x in (input().split())])
crafted_presents = {}
toy_chart = {
   150 : 'Doll',
   250 : 'Wooden train',
   300 : 'Teddy bear',
   400 : 'Bicycle'
}

while magic_values and material_boxes:
    box = material_boxes.pop()
    if box == 0:
        continue
    magic = magic_values.popleft()
    if magic == 0:
        material_boxes.append(box)
        continue
    power = magic * box

    if power in toy_chart.keys():
        if toy_chart[power] not in crafted_presents.keys():
            crafted_presents[toy_chart[power]] = 0
        crafted_presents[toy_chart[power]] += 1
        continue
    if power < 0:
        material_boxes.append(box + magic)
    else:
        material_boxes.append(box + 15)

pair_one = ['Doll', 'Wooden train']
pair_two = ['Bicycle', 'Teddy bear']

flag = False
if set(pair_one).issubset(set(crafted_presents.keys())) or set(pair_two).issubset(set(crafted_presents.keys())):
    flag = True

if flag:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f'No presents this Christmas!')

if material_boxes:
    print(f'Materials left: {", ".join([str(x) for x in material_boxes])}')
if magic_values:
    print(f'Materials left: {", ".join([str(x) for x in magic_values])}')

for key,value in crafted_presents.items():
    print(f'{key}: {value}')