number = int(input())
total = 0
for _ in range(number):
    add = int(input())
    if add + total <= 255:
        total += add
        continue
    print(f'Insufficient capacity!')

print(total)