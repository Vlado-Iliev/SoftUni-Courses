column = 2
r = 2

start, stop, step = (0, column, 1) if r % 2 == 0 else (-1, column, -1)

print(start,stop,step)