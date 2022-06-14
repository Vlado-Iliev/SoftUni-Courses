def emote_finder(data):
    emotes = [data[i] + data[i + 1] for i in range(len(data)) if data[i] == ':']
    print('\n'.join(emotes))


line = input()
emote_finder(line)