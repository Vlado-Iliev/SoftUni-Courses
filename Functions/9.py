def password_validator(passowrd):
    fault_a = False
    fault_b = False
    fault_c = False

    allowed_letters = [*range(97, 123, 1)]
    allowed_letters.extend([*range(65, 91, 1)])
    allowed_letters = list(map(chr, allowed_letters))

    allowed_numbers = [*range(48, 58, 1)]
    allowed_numbers = list(map(int, allowed_numbers))

    if 6 <= len(passowrd) <= 10:
        fault_a = False
    else:
        fault_a = True

    for l in passowrd:
        if l not in str(allowed_letters) and l not in str(allowed_numbers):
            fault_b = True

    number_counter = 0
    for l in passowrd:
        if l in str(allowed_numbers):
            number_counter += 1
    if number_counter < 2:
        fault_c = True

    if fault_a:
        print('Password must be between 6 and 10 characters')
    if fault_b:
        print('Password must consist only of letters and digits')
    if fault_c:
        print('Password must have at least 2 digits')
    if fault_a == False and fault_b == False and fault_c == False:
        print('Password is valid')


password_validator(input())
