line = input()
store = dict()
while ':' in line:
    info = line.split(': ')
    product = info[0]
    quantity = int(info[1])
    if product not in store:
        store[product] = quantity
    else:
        store[product] += quantity

    line = input()

all = len(store.keys())
total = sum(store.values())

print('Products in stock:')

for key,value in store.items():
    print(f'- {key}: {value}')

print(f'Total Products: {all}')
print(f'Total Quantity: {total}')