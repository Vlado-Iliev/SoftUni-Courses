import re

num = int(input())
regex = r'^([\$\%])([A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
for n in range(num):
    line = input()
    condition = False
    matches = re.finditer(regex,line)

    for match in matches:
        tag = match[2]
        num1 = int(match[3])
        num2 = int(match[4])
        num3 = int(match[5])
        decoded = chr(num1)+chr(num2)+chr(num3)
        condition = True

    if condition:
        print(f"{tag}: {decoded}")
    else:
        print("Valid message not found!")
