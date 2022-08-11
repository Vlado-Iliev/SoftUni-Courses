from itertools import permutations


def possible_permutations(input_list):
    for x in permutations(input_list):
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]
