from string import ascii_letters
def password_validator(data):
    allowed_letters = ''.join(ascii_letters + '-' + '_')
    for pas in data:
        if 3 <= len(pas) <= 16:
            a =[ch for ch in pas if ch in allowed_letters ]
            if len(a) == len(pas):
                print(pas)



line = input().split(', ')
password_validator(line)
