class Vehicle:
    def __init__(self,type,model,price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self,money: int, owner: str):
        if money > self.price:
            if self.owner == None:
                change = money - self.price
                self.owner = owner
                return f'Successfully bought a {self.type}. Change: {change}'
            else:
                return 'Car already sold'
        else:
            return 'Sorry, not enough money'

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return 'Vehicle has no owner'
    def __repr__(self):
        if self.owner != None:
            return f'{self.model} {self.type} is owned by: {self.owner}.'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'






type = 'car'
model = 'BMW'
price = 30000
vehicle = Vehicle(type,model, price)
print(vehicle.buy(15000, 'Peter'))
print(vehicle.buy(35000, 'George'))
print(vehicle)
vehicle.sell()
print(vehicle)