age = float(input())
gender = input()

if age<16 :
    if gender == 'm' :
        print('Master')
    elif gender == 'f' :
        print('Miss')

elif age >= 16:
    if gender == 'm' :
        print('Mr.')
    elif gender == 'f' :
        print('Ms.')
