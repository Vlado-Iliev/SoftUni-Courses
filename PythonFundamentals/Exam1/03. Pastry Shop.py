type_of_pastry = input()
number_of_pastry = int(input())
date_of_order = int(input())

if type_of_pastry == 'Cake':
    if date_of_order <= 15:
        price = 24
    else:
        price = 28.70
elif type_of_pastry == 'Souffle':
    if date_of_order <= 15:
        price = 6.66
    else:
        price = 9.80
elif type_of_pastry == 'Baklava':
    if date_of_order <= 15:
        price = 12.60
    else:
        price = 16.98
total_price = number_of_pastry * price

if date_of_order <= 22:
    if 100<= total_price <= 200:
        total_price *= 0.85
    elif total_price > 200:
        total_price *= 0.75
    if date_of_order <= 15:
        total_price *= 0.9
print(f'{total_price:.2f}')

