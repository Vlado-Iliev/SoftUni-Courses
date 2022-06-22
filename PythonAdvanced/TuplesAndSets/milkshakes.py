from collections import deque

chocoloate_bars = [int(x) for x in (input().split(', '))]
milk_cups = deque([int(x) for x in (input().split(', '))])
milkshakes_counter = 0

while chocoloate_bars and milk_cups and milkshakes_counter < 5:
    milk = milk_cups.popleft()
    chocoloate = chocoloate_bars.pop()

    if milk <= 0 and chocoloate <= 0:
        continue
    if milk <= 0:
        chocoloate_bars.append(chocoloate)
        continue
    if chocoloate <= 0:
        milk_cups.appendleft(milk)
        continue

    if milk == chocoloate:
        milkshakes_counter += 1
    else:
        milk_cups.append(milk)
        chocoloate_bars.append(chocoloate - 5)


if milkshakes_counter >= 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocoloate_bars:
    print(f'Chocolate: {", ".join([str(x) for x in chocoloate_bars])}')
else:
    print('Chocolate: empty')
if milk_cups:
    print(f'Milk: {", ".join([str(x) for x in milk_cups])}')
else:
    print('Milk: empty')
