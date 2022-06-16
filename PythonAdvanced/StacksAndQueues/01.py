word = list(input())
b = []
for _ in range(len(word)):
    b.append(word.pop())


print(''.join(b))
