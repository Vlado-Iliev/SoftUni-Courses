from collections import deque

seeds = ["rose", "tulip", "lotus", "daffodil"]
flowers = [[letter for letter in word] for word in seeds]
garden = list()
for flower in flowers:
    plant = {key: False for key in flower}
    garden.append(plant)

vowels = deque(input().split())
consonants = list(input().split())

wining_condition = False

while not wining_condition and vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for f in garden:
        if wining_condition:
            break
        for key, value in f.items():
            if key == vowel:
                f[key] = True

            if key == consonant:
                f[key] = True

        if all(value == True for value in f.values()):
            flower_found = "".join([w for w in f])
            print(f'Word found: {flower_found if flower_found != "dafoil" else "daffodil"}')
            wining_condition = True

if not wining_condition:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join([x for x in vowels])}')
if consonants:
    print(f'Consonants left: {" ".join([x for x in consonants])}')
