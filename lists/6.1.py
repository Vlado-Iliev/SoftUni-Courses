def repeat_remover(data):
    new_word = list(data[i] for i in range(len(data) - 1) if data[i] != data[i + 1] )




    print(''.join(new_word))


line = input()
repeat_remover(line)