from math import ceil
budget = float(input())
num_of_students = int(input())
price_of_flour = float(input())
price_of_egg = float(input())
price_of_apron = float(input())
total_price = 0
flower_counter = 0

for student in range(num_of_students):
    flower_counter += 1
    if flower_counter == 5:
        flower_counter = 0
        continue
    else:
        total_price += price_of_flour

total_price += num_of_students * 10 * price_of_egg
total_price += price_of_apron * (ceil(num_of_students * 1.2))

if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    needed = total_price - budget
    print(f'{needed:.2f}$ more needed.')


