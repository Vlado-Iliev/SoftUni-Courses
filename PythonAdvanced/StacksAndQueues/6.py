
line = input()
opening_brackets = list()

flag = False
for ch in line:
    if ch in '([{':
        opening_brackets.append(ch)
    else:
        current_opening = opening_brackets[-1]
        if ch ==']':
            if current_opening == '[':
                opening_brackets.pop()
            else:
                flag = True
        elif ch =='}':
            if current_opening == '{':
                opening_brackets.pop()
            else:
                flag = True
        elif ch ==')':
            if current_opening == '(':
                opening_brackets.pop()
            else:
                flag = True
        if flag:
            print('N0')
            break

if not flag:
    print('YES')
