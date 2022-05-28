from math import floor
target_num_processors = int(input())
number_of_staff = int(input())
working_days = int(input())

total_working_hours = number_of_staff * 8 * working_days
processors_made = floor(total_working_hours / 3)



if processors_made >= target_num_processors:
    extra_processors = processors_made - target_num_processors
    money_earned = extra_processors * 110.10

    print(f'Profit: -> {money_earned:.2f} BGN')
else:
    not_enough_processors = target_num_processors - processors_made
    loses = not_enough_processors * 110.10
    print(f'Losses: -> {loses:.2f} BGN')