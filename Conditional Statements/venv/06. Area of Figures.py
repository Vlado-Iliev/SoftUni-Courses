from math import pi

# if from 3 fifures
shape_input = input()

# Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
if shape_input == "square":
    side_lenght = float(input())
    area = side_lenght * side_lenght
# Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
elif shape_input == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_b * side_a
# Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
elif shape_input == "circle":
    circle_radius = float(input())
    area = pi * circle_radius * circle_radius

# Ако фигурата е триъгълник, на следващите два реда четат две числа - дължината на страната му и дължината на височината към нея.
elif shape_input == "triangle":
    side_lenght = float(input())
    hight = float(input())
    area = side_lenght * hight / 2

# пресмятане на лицата
# Резултатът да се закръгли до 3 цифри след десетичната точка.
print(f"{area:.3f}")
