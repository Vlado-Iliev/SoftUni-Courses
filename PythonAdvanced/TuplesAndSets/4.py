line = input()

letter_occurrences = dict()

for letter in line:
    if letter not in letter_occurrences:
        letter_occurrences[letter] = 0
    letter_occurrences[letter] += 1

for key,value in sorted(letter_occurrences.items()):
    print(f'{key}: {value} time/s')
