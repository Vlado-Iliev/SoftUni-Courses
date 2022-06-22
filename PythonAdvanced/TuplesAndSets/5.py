num_of_pairs = int(input())
longest_intersection = list()
for _ in range(num_of_pairs):
    a, b = [x for x in (input().split('-'))]

    start_a, finish_a = a.split(',')
    set_a = set(range(int(start_a),int(finish_a) + 1))

    start_b, finish_b = b.split(',')
    set_b = set(range(int(start_b), int(finish_b) + 1))

    current_intersection = set_a.intersection(set_b)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = list(map(int, current_intersection))

print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')