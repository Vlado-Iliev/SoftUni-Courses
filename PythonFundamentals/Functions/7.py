def printer(a):
    current_sum = sum(a)
    current_max = max(a)
    current_min = min(a)
    print(f'The minimum number is {current_min}')
    print(f'The maximum number is {current_max}')
    print(f'The sum number is: {current_sum}')





numbers = list(map(int,(input().split(' '))))
printer(numbers)