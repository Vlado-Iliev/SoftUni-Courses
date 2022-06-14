def calculator(data1, data2):
    total = 0
    for i in range(len(data1)):
        if i >= len(data2):
            total += ord(data1[i])
        else:
            total += ord(data1[i]) * ord(data2[i])

    print(total)

line = input().split(' ')

if len(line[0]) > len(line[1]):
    calculator(line[0], line[1])
else:
    calculator(line[1], line[0])
