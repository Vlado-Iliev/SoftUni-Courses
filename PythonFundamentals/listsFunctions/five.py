names = input().split(', ')

names = sorted(names,key = lambda names:(-len(names),names))

print(names)

