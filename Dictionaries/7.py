num = int(input())
words = dict()

for w in range(num):
    word = input()
    synonym = input()
    if word not in words.keys():
        words[word] = list()
        words[word].append(synonym)
    else:
        words[word].append(synonym)

for key,value in words.items():
    print(f"{key} - {', '.join(value)}")