def fibonacci():
    first = 0
    yield first
    second = 1
    yield second
    while True:
        num_one = first
        num_two = second
        value_to_return = num_one + num_two
        yield value_to_return
        first = num_two
        second = value_to_return




generator = fibonacci()

for i in range(1):

    print(next(generator))