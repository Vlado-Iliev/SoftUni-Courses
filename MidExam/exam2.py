vehicles = input().split('>>')
total = 0
for vehicle in vehicles:
    vehicle = vehicle.split(' ')
    type_of_vehicle = vehicle[0]
    num_of_years = int(vehicle[1])
    km_traveled = int(vehicle[2])
    if type_of_vehicle == 'family':
        initial_cost = 50
        price_for_travel = 12
        travel_range = 3000
        total_cost = initial_cost - (num_of_years * 5) + ((km_traveled//travel_range) * price_for_travel)

    elif type_of_vehicle == 'heavyDuty':
        initial_cost = 80
        price_for_travel = 14
        travel_range = 9000
        total_cost = initial_cost - (num_of_years * 8) + ((km_traveled // travel_range) * price_for_travel)
    elif type_of_vehicle == 'sports':
        initial_cost = 100
        price_for_travel = 18
        travel_range = 2000
        total_cost = initial_cost - (num_of_years * 9) + ((km_traveled // travel_range) * price_for_travel)
    else:
        print('Invalid car type.')
        continue
    print(f'A {type_of_vehicle} car will pay {total_cost:.2f} euros in taxes.')
    total += total_cost

print(f'The National Revenue Agency will collect {total:.2f} euros in taxes.')

