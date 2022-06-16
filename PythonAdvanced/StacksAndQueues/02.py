line = input()
opening_brackets = []
expression = ''
for i in range(len(line)):

    if line[i] == '(':
        opening_brackets.append(i)
    elif line[i] == ')':
        closing_bracket = i
        last_op_bracket = opening_brackets.pop()
        for ch in range(last_op_bracket,closing_bracket + 1):
            expression += line[ch]

        print(expression)
        expression = ''


