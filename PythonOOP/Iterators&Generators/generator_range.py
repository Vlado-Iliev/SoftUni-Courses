def genrange(start, end):
    current_num = start

    while current_num < end + 1:
        num_to_return = current_num
        yield num_to_return
        current_num += 1


print(list(genrange(1, 10)))