first_number = int(input())
second_number = int(input())


for numbers in range(first_number, second_number + 1):
    even_numbers_sum = 0
    odd_number_sum = 0
    current_number = str(numbers)
    for index, value in enumerate(current_number):
        if index % 2 != 0:
            odd_number_sum += int(value)
        else:
            even_numbers_sum += int(value)
    if even_numbers_sum == odd_number_sum:
        print(numbers, end=" ")

