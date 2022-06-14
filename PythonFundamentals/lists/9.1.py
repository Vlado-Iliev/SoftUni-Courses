from string import digits , ascii_letters

def regequit(data):
    c = list()
    d = list()
    last_digit_index = 0
    a = data
    e = ''
    f = list()
    for i in range(len(a)):
        l = a[i]
        if l in digits:
            if last_digit_index == 0:
                c.append(a[last_digit_index :i:1])

            else:
                c.append(a[last_digit_index + 1:i:1])
            last_digit_index = i
            d.append(int(a[last_digit_index]))
        if i == len(a) - 1 and l not in digits:
            c.append(a[last_digit_index + 1:i + 1:1])
    for i in range(len(c)):
        e = e +(c[i]).upper()*d[i]
        for ch in e:
            if ch not in f:
                f.append(ch)

    print(f'Unique symbols used: {len(f)}')
    print(e)


line = input()
regequit(line)