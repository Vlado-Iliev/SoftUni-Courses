from collections import deque

num_of_petrol_stations = int(input())
stations = deque()

for _ in range(num_of_petrol_stations):
    stations.append([int(x) for x in input().split()])


for attempt in range(num_of_petrol_stations):
    tank = 0
    failed = False
    for petrol,distance in stations:
        tank = tank + petrol - distance
        if tank < 0:
            failed = True
            break

    if failed:
        stations.append(stations.popleft())
    else:
        print(attempt)
        break