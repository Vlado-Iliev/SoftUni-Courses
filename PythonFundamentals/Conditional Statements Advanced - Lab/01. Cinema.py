type_of_movie = input()
rows = int(input())
columns = int(input())
income = 0
ticket_cost = 0

if type_of_movie == 'Premiere' :
    ticket_cost = 12
    income = rows * columns * ticket_cost
if type_of_movie == 'Normal' :
    ticket_cost = 7.50
    income = rows * columns * ticket_cost
if type_of_movie == 'Discount' :
    ticket_cost = 5
    income = rows * columns * ticket_cost

print(f'{income:.2f} leva')
