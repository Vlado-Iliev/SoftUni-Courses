degrees = int(input())
time_of_the_day = input()
outfit = ""
shoes = ''

if time_of_the_day == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'T - Shirt'
        shoes = 'Sandals'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif time_of_the_day == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else :
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif time_of_the_day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
