numbers = [int(input()),int(input()),int(input())]
positive = True
for n in range(len(numbers)):
    if numbers[n] < 0:
        positive = False

if positive:
    print('positive')
else:
    print('negative')

