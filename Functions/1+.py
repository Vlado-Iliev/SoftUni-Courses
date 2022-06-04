def result(a,b):
    if a == 'int':
        return 2*int(b)
    elif a == 'real':
        return f'{(float(b)*1.5):.2f}'
    elif a == 'string':
        return f'${b}$'


print(result(input(),input()))

