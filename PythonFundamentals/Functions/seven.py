def rounding(a):
    new_list = list()
    for i in range(len(a)):
        current = float(a[i])
        current = round(current)
        new_list.append(current)
    return new_list


given = input().split(' ')

print(rounding(given))