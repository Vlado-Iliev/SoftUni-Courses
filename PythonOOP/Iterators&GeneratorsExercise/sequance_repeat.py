class sequence_repeat:

    def __init__(self,sequance,number):
        self.sequance = sequance
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.number:
            raise StopIteration
        if self.index >= len(self.sequance):
            index_to_return = self.index % len(self.sequance)
        else:
            index_to_return = self.index
        value_to_return = self.sequance[index_to_return]
        self.index += 1
        return value_to_return



result = sequence_repeat('I Love Python', 3)

for item in result:

    print(item, end ='')