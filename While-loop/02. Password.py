username = input()
set_pass = input()
pas = input()
if pas == set_pass:
    print(f'Welcome {username}!')
while pas != set_pass:
    pas = input()
    if pas == set_pass:
        print(f'Welcome {username}!')
        break