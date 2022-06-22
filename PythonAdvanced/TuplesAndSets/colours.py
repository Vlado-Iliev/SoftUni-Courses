from collections import deque

line = deque(input().split())

primary_colours = ['red', 'blue', 'yellow']
secondary_colours = ["orange", "purple", "green"]
colour_chart = {
    'orange': ['red','yellow'],
    'purple': ['red','blue'],
    'green': ['blue','yellow']
}

colours_found = []

while line:
    first_string = line.popleft()
    if line:
        second_string = line.pop()
    else:
        second_string = ''

    current_word = first_string + second_string

    if current_word in primary_colours or current_word in secondary_colours:
        colours_found.append(current_word)
        continue

    reversed_word = second_string + first_string
    if reversed_word in primary_colours or reversed_word in secondary_colours:
        colours_found.append(reversed_word)
        continue

    if len(first_string) > 1:
        first_string = first_string[:-1]
        line.insert((len(line)//2),first_string)
    if len(second_string) > 1:
        second_string = second_string[:-1]
        line.insert((len(line) // 2), second_string)

for col in colours_found:
    if col in secondary_colours:
        flag = False
        if set(colour_chart[col]).issubset(set(colours_found)):
            flag = True
        if not flag:
            colours_found.remove(col)


print(colours_found)
