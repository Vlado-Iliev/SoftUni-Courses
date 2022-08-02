from abc import ABC, abstractmethod


class Animal(ABC):
    WEIGHT_GAIN_PER_PIECE_OF_FOOD = 0

    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        allowed_food = {'Owl': ['Meat'],
                        'Tiger': ['Meat'],
                        'Dog': ['Meat'],
                        'Cat': ['Vegetable', 'Meat'],
                        'Hen': ['Vegetable', 'Meat', 'Seed', 'Fruit'],
                        'Mice': ['Vegetable', 'Fruit']
                        }
        for key, value in allowed_food.items():
            if key == self.__class__.__name__:
                for f in allowed_food[key]:
                    if f == food.__class__.__name__:
                        self.weight += self.WEIGHT_GAIN_PER_PIECE_OF_FOOD * food.quantity
                        self.food_eaten += food.quantity
                return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, )
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, )
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
