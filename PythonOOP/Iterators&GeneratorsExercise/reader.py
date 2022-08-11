def read_next(*args):
    for item in args:
        for x in item:
            yield x



for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)