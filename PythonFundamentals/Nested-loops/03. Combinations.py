target_number = int(input())
number_counter = 0
flag = False

for x in range(0, target_number + 1):
    for y in range(0, target_number + 1):
        for z in range(0, target_number + 1):

            if x + y + z == target_number:
                number_counter += 1


print(number_counter)
