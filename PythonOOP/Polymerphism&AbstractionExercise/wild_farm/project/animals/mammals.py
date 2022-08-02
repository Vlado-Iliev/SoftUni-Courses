from project.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meal'


class Tiger(Mammal):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'
