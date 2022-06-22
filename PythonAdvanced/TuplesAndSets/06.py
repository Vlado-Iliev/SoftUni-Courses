numbers = list(map(int,input().split(' ')))
target_number = int(input())
iterations_counter = 0
unique_pairs = set()
# 1 5 4 2 2 3 1 3 2
for i in range(0, len(numbers)):
    current_number = numbers[i]
    if current_number >= target_number:
        iterations_counter += 1
        continue
    else:
        for index in range(i + 1,len(numbers)):
            second_number = numbers[index]
            iterations_counter += 1
            if second_number + current_number == target_number:
                unique_pairs.add(f'({current_number}, {second_number})')
                print(f'{current_number} + {second_number} = {target_number}')
                iterations_counter += 1

print(f'Iterations done: {iterations_counter}')
[print(x) for x in unique_pairs]