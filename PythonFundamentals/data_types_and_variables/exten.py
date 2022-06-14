lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

cost = 0
shield_count = 0
for _ in range(1, lost_fights + 1):
    if _ % 2 == 0:
        cost += helmet_price
    if _ % 3 == 0:
        cost += sword_price
        if _ % 2 == 0:
            cost += shield_price
            shield_count += 1
    if shield_count >= 2:
        cost += armor_price
        shield_count = 0

print(f'Gladiator expenses: {cost:.2f} aureus')
