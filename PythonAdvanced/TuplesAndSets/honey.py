from collections import deque

bees = deque([int(x) for x in (input().split())])
nectar_flowers = [int(x) for x in (input().split())]
symbols = deque(input().split())
total_honey = 0

while bees and nectar_flowers:
    current_bee = bees.popleft()
    current_nectar = nectar_flowers.pop()
    operator = symbols.popleft()

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }

    if current_bee > current_nectar:
        bees.appendleft(current_bee)
        symbols.appendleft(operator)
        continue

    total_honey += abs(operations[operator](current_bee, current_nectar))


print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar_flowers:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_flowers])}")
