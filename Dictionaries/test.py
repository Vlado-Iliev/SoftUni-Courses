a = {'a': 2}
b = input()

print(a.get(b))
if a.get(b) == None:
    print('ne')
else:
    print('da')