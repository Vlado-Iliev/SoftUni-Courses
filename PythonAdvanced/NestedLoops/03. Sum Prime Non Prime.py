command = input()
sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print('Number is negative.')
        command = input()
        continue

    if current_number <= 3 or (current_number % 2 != 0 and current_number % 3 != 0) :
        sum_of_prime_numbers += current_number
    else:
        sum_of_non_prime_numbers += current_number
    command = input()

print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime_numbers}')
