data = input().split(', ')
data = list(map(int,data))
positives = [num for num in data if num >= 0]
negatives = [num for num in data if num < 0]
even = [num for num in data if num % 2 == 0]
odd = [num for num in data if num % 2 != 0]
even = list(map(str,even))

print(f'Positive: {", ".join(map(str,positives))}')
print(f'Negative: {", ".join(map(str,negatives))}')
print(f'Even: {", ".join(map(str,even))}')
print(f'Odd: {", ".join(map(str,odd))}')


