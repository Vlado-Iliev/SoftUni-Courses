line = input().split(' ')
search_word = input().split(' ')

bakery = dict()

for i in range(0,len(line),2):
    item = line[i]
    quantity = int(line[i + 1])
    bakery[item] = quantity

for item in search_word:
    if item in bakery.keys():
        print(f'We have {bakery[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")