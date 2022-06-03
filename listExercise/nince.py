items = input().split('|')
budget = float(input())
sold =list()
sell_value = 0
total_profit = 0
condition = False
for item in range(len(items)):
    current = items[item].split('->')
    if current[0] == 'Clothes':
        if budget >= float(current[1]) and float(current[1]) <= 50:
            condition = True

    elif current[0] == 'Shoes':
        if budget >= float(current[1]) and float(current[1]) <= 35:
            condition = True

    elif current[0] == 'Accessories':
        if budget >= float(current[1]) and float(current[1]) <= 20.50:
            condition = True

    if condition:
        budget -= float(current[1])
        profit = float(current[1]) + float(current[1]) * 0.4
        total_profit += float(current[1]) * 0.4
        sell_value += profit

        sold.append(f'{profit:.2f}')

        condition = False
budget += sell_value

print(' '.join(sold))
print(f'Profit: {total_profit:.2f}')

if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
