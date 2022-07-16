class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0
        self.used = 0

    def fill(self, ml):
        if self.free_ml() < ml:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f'Glass filled with {ml} ml'

    def free_ml(self):
        return self.capacity - self.content

    def empty(self):
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        return f'{self.free_ml()} ml left'


glass = Glass()

print(glass.fill(100))

print(glass.fill(200))

print(glass.empty())

print(glass.fill(200))

print(glass.info())
