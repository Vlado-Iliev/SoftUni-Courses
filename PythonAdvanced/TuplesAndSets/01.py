line = input().split(' ')
tt = tuple(map(float,line))

num_occurences = {}

for num in tt:
    if num not in num_occurences:
        num_occurences[num] = 0
    num_occurences[num] += 1

for num,occurences in num_occurences.items():
    print(f'{num} - {occurences} times')
