money_needed_for_trip = float(input())
available_money = float(input())
spent_days_counter = 0
total_days_counter = 0
enough_money = False

while not enough_money:
    action = input()
    action_money = float(input())
    total_days_counter += 1
    if action == 'save':
        available_money += action_money
        spent_days_counter = 0
        if available_money >= money_needed_for_trip:
            enough_money = True

    elif action == 'spend':
        available_money -= action_money
        if available_money < 0:
            available_money = 0
        spent_days_counter += 1
        if spent_days_counter == 5:
            break

if enough_money:
    print(f'You saved the money for {total_days_counter} days.')
else:
    print("You can't save the money." )
    print(total_days_counter)