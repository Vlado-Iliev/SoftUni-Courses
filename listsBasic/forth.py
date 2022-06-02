number = int(input())
secret_word = input()
normal = list()
formated = list()

for n in range(number):
    current_word = input()
    if secret_word in current_word:
        formated.append(current_word)
    normal.append(current_word)

print(normal)
print(formated)
