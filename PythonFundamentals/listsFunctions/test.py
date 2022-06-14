a = [1, 3, 4, 5, 6]
b = input().split(' ')
b = list(map(int,b))

d = b[0] + b[1]
e = b[0] - b[1]

for i in range(e, d+1):
    print(i)


if d < len(a) and e >= 0:
    print('in target')

for i in range(d,e+1):
    print(i)
