def loading_bar(number):
    load_bar = list()
    dots = int(10 - (number/10))
    percents = int(number/10)
    for ch in range(percents):
        load_bar.append('%')
    for ch in range(dots):
        load_bar.append('.')

    ''.join(load_bar)
    if number < 100:
        print(f'{number}% [{"".join(load_bar)}]')
        print('Still loading...')
    else:
        print('100% Complete!')
        print(f'[{"".join(load_bar)}]')


loading_bar(int(input()))

