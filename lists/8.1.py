def game(data):
    total = 0
    for num in data:
        currnet_total = 0
        digit = int(''.join([x for x in num if x.isdigit()]))
        if num[0].isupper() :
            second_digit = int(ord(num[0]) - 64)
            currnet_total += digit / second_digit
        elif num[0].islower():
            second_digit = int(ord(num[0]) - 96)
            currnet_total += digit * second_digit
        if num[-1].isupper():
            second_digit = int(ord(num[-1]) - 64)
            currnet_total -= second_digit
        elif num[-1].islower():
            second_digit = int(ord(num[-1]) - 96)
            currnet_total += second_digit
        total += currnet_total

    print(f'{total:.2f}')


nums = input().split()
game(nums)