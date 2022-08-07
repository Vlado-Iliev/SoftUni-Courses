from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass

    def get_species(self):
        return self.species


class Cat(Animal):

    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return 'meow'


class Dog(Animal):

    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return 'woof-woof'


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

cat = Cat
animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
