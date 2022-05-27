destination = input()
while destination != 'End':
    trip_money = float(input())
    current_money = 0
    while current_money < trip_money:
       input_money = float(input())
       current_money += input_money
    print(f'Going to {destination}!')
    destination = input()