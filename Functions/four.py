def repetition(word,times):
    new_list = list()
    for i in range(times):
        new_list.append(word)

    return new_list


a = input()
b = int(input())
print(''.join((repetition(a,b))))