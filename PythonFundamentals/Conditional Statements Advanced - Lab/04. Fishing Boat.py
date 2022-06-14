group_budget = int(input())
season = input()
number_of_people = int(input())

total_price = 0
ship_rent = 0

if season == 'Summer' or season == 'Spring' or season == 'Autumn' or season == 'Winter':
    if season == 'Spring':
        ship_rent = 3000
        if number_of_people <= 6:
            ship_rent *= 0.9
        if 7 <= number_of_people <= 11:
            ship_rent *= 0.85
        if 12 <= number_of_people:
            ship_rent *= 0.75
        if number_of_people % 2 == 0:
            ship_rent *= 0.95
    elif season == 'Autumn' or season == 'Summer':
        ship_rent = 4200
        if number_of_people <= 6:
            ship_rent *= 0.9
        if 7 <= number_of_people <= 11:
            ship_rent *= 0.85
        if 12 <= number_of_people:
            ship_rent *= 0.75
        if season == 'Summer':
            if number_of_people % 2 == 0:
                ship_rent *= 0.95
    elif season == 'Winter':
        ship_rent = 2600
        if number_of_people <= 6:
            ship_rent *= 0.9
        if 7 <= number_of_people <= 11:
            ship_rent *= 0.85
        if 12 <= number_of_people:
            ship_rent *= 0.75
        if number_of_people % 2 == 0:
            ship_rent *= 0.95

if ship_rent <= group_budget:
    print(f'Yes! You have {(group_budget - ship_rent):.2f} leva left.')
else:
    print(f'Not enough money! You need {(ship_rent - group_budget):.2f} leva.')
