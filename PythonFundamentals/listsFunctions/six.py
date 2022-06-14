numbers = input().split(', ')
numbers = list(map(int,numbers))
index = list()
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        index.append(i)

print(index)

