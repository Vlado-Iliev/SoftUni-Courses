def tribonacci(a):
    tri = [1, 1, 2]
    new_number = 0

    while not len(tri) == a:
        reversed_tri = tri[::-1]
        current_wanted_num = int(reversed_tri[0]) + int(reversed_tri[1]) + int(reversed_tri[2])
        new_number += 1
        if new_number == current_wanted_num:
            tri.append(new_number)

    return tri


print(tribonacci(int(input())))
