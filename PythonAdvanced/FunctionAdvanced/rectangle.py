def rectangle(lenght, width):
    def area(a, b):
        result = a * b
        return result

    def perimeter(a, b):
        return (a + b) * 2

    if not isinstance(lenght, int) or not isinstance(width, int):
        return 'Enter valid values!'
    else:

        ract_area = area(lenght, width)
        ract_prerimeter = perimeter(lenght, width)

        return f'Rectangle area: {ract_area}\nRectangle perimeter: {ract_prerimeter}'


print(rectangle(2, 10))
