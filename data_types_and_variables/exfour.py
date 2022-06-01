num_inputs = int(input())
total = 0

for _ in range(num_inputs):
    char = input()
    total += ord(char)

print(f'The sum equals: {total}')