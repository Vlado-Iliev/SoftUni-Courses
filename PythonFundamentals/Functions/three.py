def calculator(parameter,a,b):
    if parameter == 'multiply':
        return a*b
    elif parameter == 'divide':
        return int(a/b)
    elif parameter == 'subtract':
        return a-b
    elif parameter == 'add':
        return a + b

parameter = input()
number_a = int(input())
number_b = int(input())

print(calculator(parameter,number_a,number_b))

