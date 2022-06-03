num = input().split(' ')
numbers = list(map(int,num))
remove = int(input())

for n in range(remove):
    current_min = min(numbers)
    numbers.remove(current_min)
new_list = list(map(str,numbers))
print((', ').join(new_list))