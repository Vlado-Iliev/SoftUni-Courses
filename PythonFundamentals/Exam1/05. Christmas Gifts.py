command = input()
number_of_adults = 0
number_kids = 0

while command != 'Christmas':
    years_old = int(command)
    if years_old <= 16:
        number_kids += 1
    else:
        number_of_adults += 1
    command = input()

total_for_toys = number_kids * 5
total_for_sweaters = number_of_adults * 15

print(f'Number of adults: {number_of_adults}')
print(f'Number of kids: {number_kids}')
print(f'Money for toys: {total_for_toys}')
print(f'Money for sweaters: {total_for_sweaters}')