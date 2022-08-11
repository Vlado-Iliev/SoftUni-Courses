def solution():

    def integers():  # TODO: Implement
        number = 1
        while True:
            yield number
            number += 1


    def halves():
        for i in integers():  # TODO: Implement
            return i/2

    def take(n):  # TODO: Implement
        result = []
        for num in integers(n):
            result.append(halves())

        return result



take = solution()[0]

halves = solution()[1]

print(take(5, halves()))