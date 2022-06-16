from collections import deque

customers = deque()

while True:
    line = input()
    if line == 'End':
        print(f'{len(customers)} people remaining.')
        break
    elif line == 'Paid':
        while customers:
            customer = customers.popleft()
            print(customer)

    else:
        customers.append(line)
