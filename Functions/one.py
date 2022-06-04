old_list = input().split(' ')
new_list = list()


def abs_change():
    for i in range(len(old_list)):
        new_list.append(abs(float(old_list[i])))
    print(new_list)


abs_change()