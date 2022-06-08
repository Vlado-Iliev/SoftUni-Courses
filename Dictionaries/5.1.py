def finish(storage,junk):
    for key,value in storage.items():
        print(f'{key}: {value}')
    for key,value in junk.items():
        print(f'{key}: {value}')


storage = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = dict()
while True:
    line = input().split(' ')
    items = list(map(lambda x: x.lower(),line[1::2]))
    quantity = list(map(lambda x: int(x),line[::2]))
    for item in items:
        if item in storage.keys():
            storage[item] += quantity[items.index(item)]
        elif item in junk_items.keys():
            junk_items[item] += quantity[items.index(item)]
        else:
            junk_items[item] = quantity[items.index(item)]
  #  for item in range(len(items)):
  #      if items[item] in storage.keys() or items[item] in junk_items.keys():
 #           if items[item] in storage.keys():
 #               storage[items[item]] += quantity[item]
#            elif items[item] in junk_items.keys():
#                junk_items[items[item]] += quantity[item]
#            else:
 #               junk_items[items[item]] = quantity[item]

        for key, value in storage.items():
            if storage[key] >= 250:
                storage[key] -= 250
                if key == 'shards':
                    print(f"Shadowmourne obtained!")

                elif key == 'motes':
                    print(f"Dragonwrath obtained!")

                elif key == 'fragments':
                    print(f"Valanyr obtained!")

                else:
                    continue
                finish(storage,junk_items)
                break

