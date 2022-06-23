test_hours = int(input())
test_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

earlies_time = 0
formated_arrival_time_in_minutes = 0
formated_test_time_in_minutes = 0

if 0 <= test_hours <= 23 and 0 <= test_minutes <= 59 and 0 <= arrival_hours <= 23 and 0 <= arrival_minutes <= 59:
    formated_arrival_time_in_minutes = (arrival_hours * 60) + arrival_minutes
    formated_test_time_in_minutes = (test_hours * 60) + test_minutes
    earlies_time = formated_test_time_in_minutes - 30

    if earlies_time <= formated_arrival_time_in_minutes <= formated_test_time_in_minutes:
        print('On time')
        if (formated_test_time_in_minutes - formated_arrival_time_in_minutes) == 0:
            print()
        elif (formated_test_time_in_minutes - formated_arrival_time_in_minutes) != 1:
            print(f'{(formated_test_time_in_minutes - formated_arrival_time_in_minutes)} minutes before the start')

    elif formated_arrival_time_in_minutes < earlies_time:
        print('Early')
        if (formated_test_time_in_minutes - formated_arrival_time_in_minutes) < 60:
            print(f'{(formated_test_time_in_minutes - formated_arrival_time_in_minutes) % 60} minutes before the start')
        elif (formated_test_time_in_minutes - formated_arrival_time_in_minutes) >= 60:
            if ((formated_test_time_in_minutes - formated_arrival_time_in_minutes) % 60) > 10:
                print(
                    f'{(formated_test_time_in_minutes - formated_arrival_time_in_minutes) // 60} : {(formated_test_time_in_minutes - formated_arrival_time_in_minutes) % 60} hours before the start')
            else:
                print(
                    f'{(formated_test_time_in_minutes - formated_arrival_time_in_minutes) // 60} : 0{(formated_test_time_in_minutes - formated_arrival_time_in_minutes) % 60} hours before the start')
    elif formated_arrival_time_in_minutes > formated_test_time_in_minutes:
        print('Late')
        if (formated_arrival_time_in_minutes - formated_test_time_in_minutes) < 60:
            print(f'{(formated_arrival_time_in_minutes - formated_test_time_in_minutes) % 60} minutes after the start')

        elif (formated_arrival_time_in_minutes - formated_test_time_in_minutes) >= 60:
            if ((formated_arrival_time_in_minutes - formated_test_time_in_minutes) % 60) > 10:
                print(
                    f'{(formated_arrival_time_in_minutes - formated_test_time_in_minutes) // 60} : {(formated_arrival_time_in_minutes - formated_test_time_in_minutes) % 60} hours after the start')
            else:
                print(
                    f'{(formated_arrival_time_in_minutes - formated_test_time_in_minutes) // 60} : 0{(formated_arrival_time_in_minutes - formated_test_time_in_minutes) % 60} hours after the start')
