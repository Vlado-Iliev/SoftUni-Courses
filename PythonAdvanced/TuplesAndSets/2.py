n, m = input().split(' ')
set_a = set()
set_b = set()
for _ in range(int(n)):
    set_a.add(input())

for _ in range(int(m)):
    set_b.add(input())

interceptions = set_a.intersection(set_b)
print(*interceptions, sep='\n')
