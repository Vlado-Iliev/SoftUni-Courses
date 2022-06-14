line = input()
total_net = 0
tax = 0
final_price = 0
discount = 0

while line != 'special' and line != 'regular':
    if float(line) > 0:
        total_net += float(line)
    else:
        print(f'Invalid price!')
    line = input()

tax = total_net * 0.2
if line == 'special':
    discount = (total_net + tax) * 0.1
final_price = total_net + tax - discount

if final_price <= 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_net:.2f}$")
    print(f'Taxes: {tax:.2f}$')
    print('-----------')
    print(f'Total price: {final_price:.2f}$')
