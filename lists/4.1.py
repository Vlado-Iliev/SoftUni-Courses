def cipher(data):
    text = ''.join([chr(ord(x) + 3) for x in data ])
    print(text)


line = input()
cipher(line)
