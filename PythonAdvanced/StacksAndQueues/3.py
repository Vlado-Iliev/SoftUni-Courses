from collections import deque

quantity = int(input())
queue = deque()
line = input().split(' ')
order_counter = 0
for customer in line:
    queue.append(int(customer))
print(f'{max(queue)}')
for _ in range(len(queue)):

    if quantity >= queue[0]:
        quantity -= queue[0]
        queue.popleft()
        order_counter += 1

if queue:
    queue = list(map(str,queue))
    print(f'Orders left: {" ".join(queue)}')
else:
    print('Orders complete')
