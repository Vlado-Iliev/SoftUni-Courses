search_word = input()
line = input()
while search_word in line:
    line = line.replace(search_word,'')

print(line)