
def adding(side,user):
    search = user
    if (force_users.get(search)) == None:
        pass
    else:
        force_users[user] = side
        if side in force_sides.keys():
            force_sides[side].append(user)
        else:
            force_sides[side] = list()
            force_sides[side].append(user)
            force_users[user] = side


def joining(user,side):
    if user in force_users.keys():
        force_sides[side].remove(user)
        force_users[user] = side
        force_sides[side].append(user)

    elif side in force_sides.keys():
        force_users[user] = side
        force_sides[side].append(user)

    else:
        force_users[user] = side
        force_sides[side] = list()
        force_sides[side].append(user)

    print(f'{user} joins the {side} side!')

def finishing(users,sides):
    for side in force_sides.keys():
        print(f'Side: {side}, Members: {len(force_sides[side])}')
        for member in force_sides[side]:
            print(f'! {member}')


force_users = dict
force_sides = dict

while True:
    line = input()
    if line == 'Lumpawaroo':
        finishing(force_users,force_sides)
        break

    elif '|' in line:
        side, user = line.split(' | ')
        adding(side, user)

    if '->' in line:
        user, side = line.split(' -> ')
        joining(user,side)

