from collections import Counter


word = Counter(input())

for key,value in word.items():
    if key != ' ':
        print(f"{key} -> {value}")