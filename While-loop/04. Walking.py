goal_reached = False
total_steps = 0

while not goal_reached:
    action = input()
    if action == 'Going home':
        total_steps += int(input())
        if total_steps >= 10000:
            goal_reached = True
        break
    else:
        total_steps += int(action)
        if total_steps >= 10000:
            goal_reached = True

differance = abs(total_steps - 10000)
if goal_reached:
    print('Goal reached! Good job!')
    print(f'{differance} steps over the goal!')
else:
    print(f'{differance} more steps to reach goal.')
