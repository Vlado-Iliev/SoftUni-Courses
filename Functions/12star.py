def factorial(a,b):
    list_a = list()
    sum_a = 1
    list_b = list()
    sum_b = 1

    if a == 0:
        list_a.append(1)
    for n in range(a, 0, -1):
        list_a.append(n)
    for n in list_a:
        sum_a *= n

    if b == 0:
        list_b.append(1)
    for n in range(b, 0, -1):
        list_b.append(n)
    for n in list_b:
        sum_b *= n

    return f'{(sum_a/sum_b):.2f}'


print(factorial(int(input()),int(input())))
