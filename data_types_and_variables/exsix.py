number = int(input())

for z in range(97, number + 97):
    for x in range(97, number + 97):
        for y in range(97, number + 97):
            print(f'{chr(z)}{chr(x)}{chr(y)}')

