def calculate_between_two(line):
    parts = line.split(' ')
    num_one = float(parts[0])
    num_two = int(parts[2])
    operation = parts[1]
    if operation == '^':
        return f'{(num_one**num_two):.2f}'
    if operation == '*':
        return f'{(num_one*num_two):.2f}'
    if operation == '/':
        return f'{(num_one/num_two):.2f}'
    if operation == '+':
        return f'{(num_one+num_two):.2f}'
    if operation == '-':
        return f'{(num_one-num_two):.2f}'

