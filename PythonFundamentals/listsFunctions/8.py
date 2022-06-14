def decoder(words):
    sentance = list()
    for word in words:
        number = list()
        string = list()
        for l in word:
            if l.isdigit():
                number.append(l)
            else:
                string.append(l)
        ascci =chr(int(''.join(number)))
        x = len(string) - 1
        string[0], string[x] = string[x], string[0]
        rest = ''.join(string)
        current_word = [ascci,rest]
        sentance.append(''.join(current_word))

    return ' '.join(sentance)


data = input().split(' ')
print(decoder(data))

