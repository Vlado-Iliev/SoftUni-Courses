from collections import deque

line = deque(input().split())
operators = '+-*/'
numbers = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for ch in line:
    if ch in operators:
        for _ in range(len(numbers) - 1):
            a = numbers.popleft()
            b = numbers.popleft()
            result = operations[ch](a, b)
            numbers.appendleft(result)

    else:
        numbers.append(int(ch))

print(numbers[0])
