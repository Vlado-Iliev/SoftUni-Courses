from project.animals.animal import Bird


class Owl(Bird):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

