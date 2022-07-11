

def rhombus(n):
    for i in range(n):
        print(' ' * (n-1-i) + '* '* (i+1))
    for i in range(n-2,-1,-1):
        print(' ' * (n-1-i) + '* '* (i+1))


rhombus(int(input()))