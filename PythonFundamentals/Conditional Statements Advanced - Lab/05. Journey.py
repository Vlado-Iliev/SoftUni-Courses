budget = float(input())
season = input()

type_vaccation = ''
destination = ''
cost = 0

if season == 'summer' :
    type_vaccation = 'Camp'
    if budget <=100 :
        destination = 'Bulgaria'
    elif 100 < budget <= 1000:
        destination = 'Balkans'
    else:
        destination = 'Europe'
    if destination == 'Europe':
        type_vaccation = 'Hotel'


elif season == 'winter' :
    type_vaccation = 'Hotel'
    if budget <=100 :
        destination = 'Bulgaria'
    elif 100 < budget <= 1000:
        destination = 'Balkans'
    else:
        destination = 'Europe'

if destination == "Balkans" or destination == 'Bulgaria' or destination == 'Europe':
    if destination == 'Bulgaria':
        if season == "summer" :
            cost = budget * 0.3
        else :
            cost = budget * 0.7
    elif destination == 'Balkans' :
        if season == "summer" :
            cost = budget * 0.4
        else :
            cost = budget * 0.8
    elif destination == 'Europe' :
        cost = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{type_vaccation} - {cost:.2f}')