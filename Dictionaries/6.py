line = input().split(' ')
line = list(map(lambda x: x.lower(),line))
apearance = dict()

for sym in line:
    if sym not in apearance.keys():
        apearance[sym] = 1
    else:
        apearance[sym] += 1
odd_list = list()
for sym in apearance.keys():
    if apearance[sym] % 2 != 0:
        odd_list.append(sym)


print(' '.join(odd_list))