from collections import deque

kids = deque()
line = input().split(' ')
for kid in line:
    kids.append(kid)

skip = int(input())

counter = 0
while len(kids) > 1:
    counter += 1
    if counter < skip:
        kid = kids.popleft()
        kids.append(kid)

    if counter >= skip:
        kid = kids.popleft()
        print(f'Removed {kid}')
        counter = 0


winner = kids.popleft()
print(f'Last is {winner}')
