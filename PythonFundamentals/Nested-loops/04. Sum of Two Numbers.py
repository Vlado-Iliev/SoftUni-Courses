first_number = int(input())
second_number = int(input())
magic_number = int(input())

summ = 0

flag = False

while summ != magic_number:
    combination_counter = 0
    for x in range(first_number, second_number + 1):
        for y in range(first_number, second_number + 1):
            summ = x + y
            combination_counter += 1
            if summ == magic_number:
                combination_counter += 1
                flag = True
                break
        if flag:
            break
    if flag:
        print(f'Combination N:{combination_counter - 1} ({x} + {y} = {magic_number})')
        break

    else:
        print(f'{combination_counter} combinations - neither equals {magic_number}')
        break

