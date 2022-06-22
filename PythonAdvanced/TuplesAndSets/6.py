
#read n lines
#find the summ of the lines and devide it by n
#if result is odd or even add to specific set
#depending on the differences of the sets print

n = int(input())
even_set = set()
odd_set = set()
for i in range(1, n + 1):
    line = input()
    current_sum = sum([ord(x) for x in line]) // i
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

sum_even = sum(even_set)
sum_odd = sum(odd_set)

if sum_even == sum_odd:
    result = even_set | odd_set
    print(*result, sep=', ')
elif sum_even > sum_odd:
    result = even_set ^ odd_set
    print(*result, sep=', ')
else:
    result =  odd_set - even_set
    print(*result, sep=', ')
