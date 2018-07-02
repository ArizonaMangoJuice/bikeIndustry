from bikeShop import BikeShop

class Customer(object):
    def __init__(self, name = 'genericCustomer', funds = 0, bikes = {}):
        self.name = name
        self.funds = funds
        self.bikes = {}
        
    def buyingOptions(self, store):
        for item in store.inventory:
            if(store.inventory[item].price <= self.funds):
                print(store.inventory[item].name)
    
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
            print(self.bikes)
        else: 
            print('You don\'t have sufficient funds')