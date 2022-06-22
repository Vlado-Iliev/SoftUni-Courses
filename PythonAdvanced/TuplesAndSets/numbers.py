first_set = set(input().split())
second_set = set(input().split())
n = int(input())

for _ in range(n):
    command = input().split()
    operation = command[0]
    regarding_set = command[1]

    if operation == 'Add':
        numbers = command[2:]
        if regarding_set == 'First':
            [first_set.add(x) for x in numbers]
        else:
            [second_set.add(x) for x in numbers]

    elif operation == 'Remove':
        numbers = command[2:]
        if regarding_set == 'First':
            [first_set.remove(x) for x in numbers if x in first_set]
        else:
            [second_set.remove(x) for x in numbers if x in second_set]
    else:
        print(second_set.issubset(first_set))

print(', '.join([x for x in sorted(first_set)]))
print(', '.join([x for x in sorted(second_set)]))



