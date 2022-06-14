stock = input()
city = input()
quantity = float(input())
price = 0
total = 0
if city == 'Sofia':
    if stock == "coffee":
        price = 0.50
    elif stock == "water":
        price = 0.80
    elif stock == "beer":
        price = 1.20
    elif stock == "sweets":
        price = 1.45
    elif stock == "peanuts":
        price = 1.60
elif city == 'Varna':
    if stock == "coffee":
        price = 0.45
    elif stock == "water":
        price = 0.70
    elif stock == "beer":
        price = 1.10
    elif stock == "sweets":
        price = 1.35
    elif stock == "peanuts":
        price = 1.55
elif city == 'Plovdiv':
    if stock == "coffee":
        price = 0.40
    elif stock == "water":
        price = 0.70
    elif stock == "beer":
        price = 1.15
    elif stock == "sweets":
        price = 1.30
    elif stock == "peanuts":
        price = 1.50
total = price * quantity
print(total)