class Bicycle(object):
    def __init__(self, name = 'Generic Bike', weight = 50, price = 500):
        self.name = name
        self.weight = weight
        self.price = price
        
    def cost(self):
        print('$' + str(self.price))

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
        margin = price/3
        sellPrice = margin + price
        self.profit += margin
        del(self.inventory[name])
        # print(sellPrice)
        
    def checkProfit(self):
        print(self.profit)
        
class Customer(object):
    def __init__(self, name = 'genericCustomer', funds = 0, bikes = {}):
        self.name = name
        self.funds = funds
        self.bikes = bikes
    
    def buyBike(self, store, bikeName):
        if(store.inventory[bikeName] and self.funds >= store.inventory[bikeName].price):
            bikeDetails = {
                'name' : store.inventory[bikeName].name, 
                'weight' : store.inventory[bikeName].weight,
                'price' : store.inventory[bikeName].price
                }
            self.bikes[bikeName] = bikeDetails
            store.sellBike(bikeName)
            print('Thank you for your purchase')
        

if __name__ == '__main__':
    # redBike = Bicycle('huffer', 289, 1400)
    # redBike.name = 'huffer'
    # print(redBike.name)
    # redBike.cost()
    store = BikeShop()
    store.addBike('isael', 40, 450)
    store.addBike('isael1', 40, 450)
    # store.sellBike('isael')
    # store.sellBike('isael1')
    # store.checkInventory()
    # store.checkProfit()
    customer0 = Customer('test', 1000)
    customer0.buyBike(store, 'isael')
    store.checkInventory()
    # customer0.buyBike(store, 'isael1')
    
    
    

    