line = input().split(' ')

bakery = dict()

for i in range(0,len(line),2):
    item = line[i]
    quantity = int(line[i + 1])
    bakery[item] = quantity

print(bakery)