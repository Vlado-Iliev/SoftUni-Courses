type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

price_of_flower = 0
total_cost = 0

if type_of_flower == 'Roses' or type_of_flower == 'Dahlias' or type_of_flower == 'Tulips' or type_of_flower == 'Narcissus' or type_of_flower == 'Gladiolus' :
    if type_of_flower == 'Roses':
        price_of_flower = 5
        total_cost = price_of_flower * number_of_flowers
        if number_of_flowers > 80:
            total_cost *= .90
    elif type_of_flower == 'Dahlias':
        price_of_flower = 3.80
        total_cost = price_of_flower * number_of_flowers
        if number_of_flowers > 90:
            total_cost *= .85
    elif type_of_flower == 'Tulips':
        price_of_flower = 2.80
        total_cost = price_of_flower * number_of_flowers
        if number_of_flowers > 80:
            total_cost *= .85
    elif type_of_flower == 'Narcissus':
        price_of_flower = 3
        total_cost = price_of_flower * number_of_flowers
        if number_of_flowers < 120:
            total_cost *= 1.15
    elif type_of_flower == 'Gladiolus':
        price_of_flower = 2.50
        total_cost = price_of_flower * number_of_flowers
        if number_of_flowers < 80:
            total_cost *= 1.20

if total_cost <= budget :
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {(budget - total_cost):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_cost - budget):.2f} leva more.')