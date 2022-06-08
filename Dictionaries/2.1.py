storage = dict()

while True:
    item = input()
    if item == 'stop':
        break
    quantity = int(input())
    if item not in storage.keys():
        storage[item] = quantity
    else:
        storage[item] += quantity

for key,value in storage.items():
    print(f'{key} -> {value}')