input_number = int(input())
for current_number in range(1111,10000):
    number_is_special = True
    for index, value in enumerate(str(current_number)):
        if (int(value)) == 0:
            number_is_special = False
            continue
        if input_number % (int(value)) != 0:
            number_is_special = False
    if number_is_special:
        print(current_number, end=" ")