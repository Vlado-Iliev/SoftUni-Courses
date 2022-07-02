import string
def line_counter(line):
    punctuation_count = 0
    letters_count = 0
    for char in line:
        if char in string.punctuation:
            punctuation_count += 1
        elif char in string.ascii_letters:
            letters_count += 1

    return letters_count,punctuation_count


with open('./text.txt', 'r') as file:
    for idx, line in enumerate(file):
        letters,punctuation = line_counter(line)
        print(f'Line {idx + 1}: {line.strip()} ({letters})({punctuation})')
