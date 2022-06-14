from math import floor
type_of_year = input()
p = int(input())
h = int(input())

bonus_games = 0
free_weekends = 48 - h

saturday_games = 0.75 * free_weekends
sunday_games = h
holidays_games = p * 2/3
total_games = sunday_games + saturday_games + holidays_games

if type_of_year == 'leap':
    bonus_games = total_games * 0.15
print(f'{floor( total_games + bonus_games) }')