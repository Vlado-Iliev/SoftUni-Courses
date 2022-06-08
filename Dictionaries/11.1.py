def finishing(info):
    sides = dict()
    for key,value in info.items():
        if value not in sides.keys:
            sides[value] = list()
            sides[value].append(key)
        else:
            sides[value].append(key)
    for key,value in sides.items():
        print(f'Side:{key}, Members: {len(value)}')
        for n in range(len(value)):
            print(f'! {value[n]}')



def changing(user,side):
    force_book[user] = side
    print(f'{user} joins the {side} side')




def adding(side,user):

        force_book[user] = side
    else:
        for key in force_book.keys():
            if key == user:
                continue
            else:
                force_book[user] = side



force_book = dict

while True:
    line = input()
    if line == 'Lumpawaroo':
        finishing(force_book)
        break
    if '->' in line:
        user, side = line.split(' -> ')
        changing(user,side)

    elif '|' in line:
        side, user = line.split(' | ')
        adding(side, user)
