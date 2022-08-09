def squares(n):
    value = 1
    while value < n + 1:
        value_to_return = value*value
        yield value_to_return
        value += 1



print(list(squares(5)))