def printer(storage_content):
    for key,value in storage_content.items():
        print(f'{key} -> {value[0] * value[1]:.2f}')


storage_content = dict()

while True:
    line = input()
    if line == 'buy':
        printer(storage_content)
        break
    line = line.split(' ')
    name = line[0]
    price = line[1]
    quantity = line[2]

    if name not in storage_content.keys():
        storage_content[name] = [float(price),int(quantity)]
    else:
        storage_content[name] = [float(price), int(quantity) + storage_content[name][1]]
