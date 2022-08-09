class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_num = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num > self.end:
            raise StopIteration
        num_to_return = self.current_num
        self.current_num += 1
        return num_to_return


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
