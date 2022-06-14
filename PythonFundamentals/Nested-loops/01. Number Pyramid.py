input_number = int(input())
current_number = 1
everything_printed = False
for row in range(1, input_number + 1):
    for column in range(1, row + 1):
        if current_number > input_number:
            everything_printed = True
            break
        print(current_number, end=" ")
        current_number += 1
    print()
    if everything_printed:
        break


