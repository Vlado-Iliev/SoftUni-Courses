test_hours = int(input())
test_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

arrival_time = (arrival_hours * 60) + arrival_minutes
test_time = (test_hours * 60) + test_minutes

if arrival_time > test_time :
    print('Late')
elif test_time - 30 <= arrival_time <= test_time:
    print('On time')
else :
    print('Early')
if test_time - 60 < arrival_time < test_time :
    print(f'{test_time - arrival_time} minutes before the start')
elif arrival_time <= test_time - 60:
    difference = test_time - arrival_time
    hours = difference // 60
    minutes = difference % 60
    print(f'{hours}:{minutes:0>2d} hours before the start')
elif test_time < arrival_time <test_time + 60 :
    print(f'{arrival_time-test_time} minutes after the start')
elif arrival_time >= test_time + 60 :
    difference = arrival_time - test_time
    hours = difference // 60
    minutes = difference % 60
    print(f'{hours}:{minutes:0>2d} hours after the start')

