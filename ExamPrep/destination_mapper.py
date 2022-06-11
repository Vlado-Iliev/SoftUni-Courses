import re

line = input()

regex = r'([=/])([A-Z][a-z]{2,})\1'
matches = re.finditer(regex,line)
output = list()
len_counter = 0

for match in matches:
    output.append(match[2])
    len_counter += len(match[2])

print(f'Destinations: {", ".join(output)}')
print(f'Travel Points: {len_counter}')
