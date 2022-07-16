class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def set_radius(self, new_r):
        self.r = new_r

    def get_area(self):
        return self.r * self.r * self.pi

    def get_circumference(self):
        return (2 * self.pi) * self.r


circle = Circle(4)

circle.set_radius(160)

print(circle.r)
print(circle.get_circumference())
