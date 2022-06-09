def explosives(data):
    explosive = 0
    new_word=[]
    for i in range(len(data)):
        if data[i] == '>':
            explosive += int(data[i+1])
        if explosive > 0:
            if data[i] =='>':
                new_word.append(data[i])
            else:
                explosive -= 1
                continue
        else:
            new_word.append(data[i])

    print(''.join(new_word))

line = input()
explosives(line)