from string import digits
c = list()
last_digit_index = 0
a = 'asdad2asdasd4asd'
for i in range(len(a)):
    l = a[i]
    if l in digits:
        c.append(a[last_digit_index + 1:i:1])
        last_digit_index = i
    if i == len(a) - 1 :
        c.append(a[last_digit_index + 1:i + 1:1])

print(c)