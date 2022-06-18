input_one = int(input())
input_two = int(input())

for first in range(1, input_one + 1):
    for second in range(1, input_one + 1):
        for third in range(97, 97 + input_two):
            for fourth in range(97, 97 + input_two):
                for fifth in range(2, input_one + 1):
                    if fifth > first and fifth > second:
                        print(f'{first}{second}{chr(third)}{chr(fourth)}{fifth}', end=" ")
