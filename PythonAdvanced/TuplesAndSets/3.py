n = int(input())

unique_values = set()

for _ in range(n):
    [unique_values.add(x) for x in (input().split(' '))]

print(*unique_values , sep='\n')
