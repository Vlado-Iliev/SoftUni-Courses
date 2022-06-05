def filt(data,sentance):
    new_list = list()
    for word in data:
        if word in sentance:
            new_list.append(word)

    return new_list

data = input().split(', ')
sentance = input()
print(filt(data,sentance))
