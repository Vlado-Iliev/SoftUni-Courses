month = input()
number_of_nights = int(input())

price_of_studio = 0
price_of_apartment = 0

if month == "May" or month == 'October':
    price_of_studio = 50 * number_of_nights
    price_of_apartment = 65 * number_of_nights

    if 7 < number_of_nights <= 14:
        price_of_studio *= 0.95
    elif 14 < number_of_nights:
        price_of_studio *= 0.70
        price_of_apartment *= 0.9

elif month == "June" or month == 'September':
    price_of_studio = 75.2 * number_of_nights
    price_of_apartment = 68.70 * number_of_nights
    if 14 < number_of_nights:
        price_of_studio *= 0.80
        price_of_apartment *= 0.9
elif month == "July" or month == 'August':
    price_of_studio = 76 * number_of_nights
    price_of_apartment = 77 * number_of_nights
    if 14 < number_of_nights:
        price_of_apartment *= 0.9

print(f'Apartment: {price_of_apartment:.2f} lv.')
print(f'Studio: {price_of_studio:.2f} lv.')
