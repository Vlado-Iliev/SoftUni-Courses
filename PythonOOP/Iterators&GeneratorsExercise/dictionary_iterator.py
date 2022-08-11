class dictionary_iter:
    def __init__(self,dictionary):
        self.dictionary = dictionary
        self.index = 0
        self.dict_list = list(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.index < len(self.dictionary):
            raise StopIteration
        value_to_return = self.dict_list[self.index]
        self.index += 1
        return value_to_return



result = dictionary_iter({"name": "Peter","age": 24})

for x in result:

    print(x)