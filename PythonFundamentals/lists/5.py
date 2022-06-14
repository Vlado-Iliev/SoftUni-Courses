text = input()
digit = ''
letters = ''
char = ''
for ch in text:
    if ch.isdigit():
        digit = digit + ch
    elif ch.isalpha():
        letters = letters + ch
    else:
        char = char + ch

print(digit)
print(letters)
print(char)