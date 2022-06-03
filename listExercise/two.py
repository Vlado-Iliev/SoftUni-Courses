factor = int(input())
number_count = int(input())
list = []

for num in range(1,number_count+1):
    new_number = num * factor
    list.append(new_number)

print(list)