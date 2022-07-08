def sum_of_word(word):
    return sum([ord(letter) for letter in word])


def words_sorting(*args):
    result = f''
    dictionary = dict()
    for word in args:
        total_sum = sum_of_word(word)
        dictionary[word] = total_sum

    dict_sum = sum([x for x in dictionary.values()])
    if dict_sum % 2 == 0:
        for key, value in sorted(dictionary.items(),key=lambda x: x[0]):
            result = result + f'{key} - {value} \n'

    else:
        for key, value in sorted(dictionary.items(),key=lambda x: x[1], reverse= True ):
            result = result + f'{key} - {value} \n'
    return result


print(words_sorting('escape', 'charm', 'mythology'))

print(words_sorting('escape','charm','eye'))

print(words_sorting('cacophony','accolade'))
