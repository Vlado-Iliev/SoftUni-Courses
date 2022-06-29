def operate(operator, a, *args):
    result = a
    for x in args:
        if operator == '+':
            result += x
        elif operator == '-':
            result -= x
        elif operator == '*':
            result *= x
        elif operator == '/':
            result/= x
    return result

print(operate("*", 3, 4))