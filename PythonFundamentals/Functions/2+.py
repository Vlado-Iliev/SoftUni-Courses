def closest_point_two(a,b,c,d):
    point_a = abs(0 - a)
    point_b= abs(0 - b)
    point_c = abs(0 - c)
    point_d = abs(0 - d)

    point_x = point_a + point_b
    point_y = point_c + point_d

    if point_x < point_y:
        print(f'({int(a)}, {int(b)})')
    elif point_x > point_y:
        print(f'({int(c)}, {int(d)})')
    elif point_x == point_y:
        print(f'({int(a)}, {int(b)})')


a,b,c,d = float(input()),float(input()),float(input()),float(input())
closest_point_two(a,b,c,d)