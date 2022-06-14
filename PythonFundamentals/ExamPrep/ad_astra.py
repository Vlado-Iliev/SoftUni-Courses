import re

regex = r'([\#\|])([A-Z a-z \s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
line = input()
total_calories = 0
fridge = dict()

matches = re.finditer(regex,line)

for match in matches:
    total_calories += int(match[4])
    fridge[match[2]] = [match[3],int(match[4])]


days = total_calories//2000
print(f'You have food to last you for: {days} days!')

for key,value in fridge.items():
    print(f'Item: {key}, Best before: {value[0]}, Nutrition: {value[1]}')
