from bicycles import Bicycle

class BikeShop(object):
    def __init__(self, name = 'genericBikeShop', inventory = {}, profit = 0):
        self.name = name
        self.inventory = inventory
        self.profit = profit
    
    def checkInventory(self):
        for item in self.inventory:
            bike = {
                'name' : self.inventory[item].name, 
                'weight' : self.inventory[item].weight, 
                'price' : self.inventory[item].price
            }
            print(bike)
        
    def addBike(self, name, weight, price):
        newBike = Bicycle(name, weight, price)
        self.inventory[name] = newBike
        # self.checkInventory()
        # type(self.inventory)
        
    def sellBike(self, name):
        price = self.inventory[name].price
        margin = price/5
        sellPrice = margin + price
        self.profit += margin
        del(self.inventory[name])
        # print(sellPrice)
        
    def checkProfit(self):
        print(self.profit)