class Bicycle(object):
    def __init__(self, name = 'Generic Bike', weight = 50, price = 500):
        self.name = name
        self.weight = weight
        self.price = price
        
    def cost(self):
        print('$' + str(self.price))