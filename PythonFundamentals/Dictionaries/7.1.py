def register(username, reg):
    if username in parking_lot.keys():
        print(f'ERROR: already registered with plate number {parking_lot[username]}')
    else:
        parking_lot[username] = reg
        print(f'{username} registered {reg} successfully')


def unregister(user):
    if user not in parking_lot.keys():
        print(f'ERROR: user {user} not found')
    else:
        print(f'{user} unregistered successfully')
        del parking_lot[user]


parking_lot = dict()
n = int(input())
for n in range(n):
    line = input().split(' ')
    function = line[0]
    username = line[1]
    if function == 'register':
        reg = line[2]
        register(username,reg)
    elif function == 'unregister':
        unregister(username)

for key,value in parking_lot.items():
    print(f'{key} => {value}')
