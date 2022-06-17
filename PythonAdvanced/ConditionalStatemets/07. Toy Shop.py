# Вход
    # 1. Цена на екскурзията - реално число;
trip_cost = float(input())
    # 2. Брой пъзели - цяло число;
num_puzzels = int(input())
    # 3. Брой говорещи кукли - цяло число;
num_dolls = int(input())
    # 4. Брой плюшени мечета - цяло число;
num_teddies = int(input())
    # 5. Брой миньони - цяло число;
num_minions = int(input())
    # 6. Брой камиончета - цяло число.
num_trucks = int(input())
    # пресмятане
profit = (num_puzzels * 2.6) + (num_dolls * 3) + (num_teddies * 4.1) + (num_minions * 8.2) + (num_trucks * 2)
num_toys = num_trucks + num_minions + num_teddies + num_teddies + num_dolls + num_puzzels

if num_toys >= 50:
    profit = profit * 0.75
rent = profit * 0.10
total_profit = profit - rent
# резултата според печалба
if total_profit >= trip_cost:
    money_left = total_profit - trip_cost
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = trip_cost - total_profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")
