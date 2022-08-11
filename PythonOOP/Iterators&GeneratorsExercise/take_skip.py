class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        number_to_return = self.current_number
        self.current_number += self.step
        self.count -= 1
        return number_to_return


numbers = take_skip(10, 5)

for number in numbers:
    print(number)
