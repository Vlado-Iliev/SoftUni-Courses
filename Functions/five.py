def total_price(product,quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity * 1.0
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'snacks':
        return quantity * 2.0

a = input()
b = int(input())

print(f'{total_price(a,b):.2f}')
