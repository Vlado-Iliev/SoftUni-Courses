class Zoo:
    _animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == 'mammals':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.bird.append(name)

    def get_info(self, species):
        if species == 'mammal':
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}")
        elif species == 'fish':
            print(f"Fish in {self.zoo_name}: {', '.join(self.fish)}")
        elif species == 'bird':
            print(f"Bird in {self.zoo_name}: {', '.join(self.bird)}")
        zoo._animals += 1


zoo = Zoo(input())
animals = int(input())
for animal in range(animals):
    command = input().split(' ')
    zoo.add_animal(command[0], command[1])

zoo.get_info(input())
print(f"Total animals: {Zoo._animals}")

