passengers_from_start = int(input())
number_of_stops = int(input())

current_passengers = passengers_from_start

for stops in range (1, number_of_stops + 1):
    passengers_leaving = 0
    passengers_comming = 0
    if stops % 2 == 1:
        passengers_comming += 2
        passengers_leaving = int(input())
        passengers_comming += int(input())
    else:
        passengers_leaving = int(input())
        passengers_comming += int(input())
        passengers_leaving += 2

    if passengers_leaving > passengers_comming:
        current_passengers -= passengers_leaving - passengers_comming
    else:
        current_passengers += passengers_comming - passengers_leaving
print(f'The final number of passengers is : {current_passengers}')

