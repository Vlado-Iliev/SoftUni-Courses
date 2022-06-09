line = input()
while line != 'end':
    rev_word = line[::-1]
    print(f'{line} = {rev_word}')

    line = input()