number = int(input())
positive = list()
positive_count = 0
negative = list()
negative_sum = 0

for n in range(number):
    current = int(input())
    if current >= 0:
        positive.append(current)
        positive_count += 1
    else:
        negative.append(current)
        negative_sum += current

print(positive)
print(negative)
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negative_sum}')