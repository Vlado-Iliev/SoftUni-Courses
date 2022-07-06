def triangle_print(number):
    if not number.isdigit():
        return print(f'Invalid input!')
    number = int(number)
    for n in range(number + 1):
        for sn in range(1,n + 1):
            print(f'{sn}',end=' ')
        print()
    for n in range(number,-1,-1):
        for sn in range(1,n):
            print(f'{sn}',end=' ')
        print()



