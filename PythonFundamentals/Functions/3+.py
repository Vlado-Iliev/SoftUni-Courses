def closest_point_two(a, b, c, d, e, f, g, h):
    point_a = abs(0 - a)
    point_b = abs(0 - b)
    point_c = abs(0 - c)
    point_d = abs(0 - d)
    point_e = abs(0 - e)
    point_f = abs(0 - f)
    point_g = abs(0 - g)
    point_h = abs(0 - h)

    point_x = sum([int(point_a), int(point_b)])
    point_y = sum([int(point_c), int(point_d)])
    point_z = sum([int(point_e), int(point_f)])
    point_q = sum([int(point_g), int(point_h)])

    points = [point_x, point_y, point_z, point_q]
    points.sort()

    print(f'({", ".join(map(str, (points[2])))}) ({", ".join(map(str, (points[3])))})')


a, b, c, d, e, f, g, h = float(input()), float(input()), float(input()), float(input()), float(input()), float(
    input()), float(input()), float(input())
closest_point_two(a, b, c, d, e, f, g, h)
