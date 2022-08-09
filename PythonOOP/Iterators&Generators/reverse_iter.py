class reverse_iter:
    def __init__(self, nums):
        self.nums = nums
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < -len(self.nums):
            raise StopIteration
        index_to_return = self.current_index
        self.current_index -= 1
        return self.nums[index_to_return]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
