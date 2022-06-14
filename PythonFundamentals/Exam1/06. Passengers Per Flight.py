from sys import maxsize
from math import floor
number_of_companies = int(input())
best_average = -maxsize
best_company = ''
for company in range(1, number_of_companies + 1):
    company_name = input()
    command = input()
    total_passengers = 0
    total_flights = 0
    while command != 'Finish':
        total_flights += 1
        total_passengers += int(command)
        command = input()
        average_passengers = floor(total_passengers / total_flights)
    print(f'{company_name}: {average_passengers} passengers.')
    if average_passengers > best_average:
        best_average = average_passengers
        best_company = company_name
print(f'{best_company} has most passengers per flight: {best_average}')