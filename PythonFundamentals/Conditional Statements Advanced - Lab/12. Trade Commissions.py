city = input()
sales =  float(input())
commision = 0
total = 0
if city == 'Sofia':
    if 0 <= sales <=500:
        commision = 0.05
    elif 500 < sales <= 1000:
        commision = 0.07
    elif 1000 < sales <= 10000:
        commision = 0.08
    elif 10000 < sales:
        commision = 0.12
    else:
        print('error')

elif city == 'Varna':
    if 0 <= sales <=500:
        commision = 0.045
    elif 500 < sales <= 1000:
        commision = 0.075
    elif 1000 < sales <= 10000:
        commision = 0.10
    elif 10000 < sales :
        commision = 0.13
    else:
        print('error')

elif city == 'Plovdiv':
    if 0 <= sales <=500:
        commision = 0.055
    elif 500 < sales <= 1000:
        commision = 0.08
    elif 1000 < sales <= 10000:
        commision = 0.12
    elif 10000 < sales :
        commision = 0.145
    else:
        print('error')
else :
    print('error')
if not commision == 0 :
    total = sales * commision
    print(f'{total:.2f}')