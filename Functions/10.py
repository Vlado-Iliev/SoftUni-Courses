def perf_number(number):
    number_is_perfect = True
    num_sum = 0
    deviders = list()

    if number < 0:
        number_is_perfect = False
    else:
        for n in range(1, number):
            if number % n == 0:
                deviders.append(n)
    if not sum(deviders) == number:
        number_is_perfect = False

    if number_is_perfect:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


print(perf_number(int(input())))