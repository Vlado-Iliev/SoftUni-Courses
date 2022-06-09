line = input().split(' ')
word = ''
for w in line:
    add = ''
    add = w * len(w)
    word = word + add
print(word)