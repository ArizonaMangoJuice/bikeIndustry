from bicycles import Bicycle
from bikeShop import BikeShop
from customer import Customer
store = BikeShop()
    
if __name__ == '__main__':
    # redBike = Bicycle('huffer', 289, 1400)
    # redBike.name = 'huffer'
    # print(redBike.name)
    # redBike.cost()
    store = BikeShop()
    
    store.addBike('isael', 40, 450)
    store.addBike('isael1', 45, 550)
    store.addBike('isael2', 50, 650)
    store.addBike('isael3', 55, 700)
    store.addBike('isael4', 60, 150)
    
    customer0 = Customer('test', 1000)
    customer1 = Customer('test1', 500)
    customer2 = Customer('test2', 200)
    
    print('customer 0 buying options')
    customer0.buyingOptions(store)
    print('customer 1 buying options')
    customer1.buyingOptions(store)
    print('customer 2 buying options')
    customer2.buyingOptions(store)
    
    print('Available inventory')
    store.checkInventory()
    
    print('customer0 purchase')
    customer0.buyBike(store, 'isael3')
    print('customer1 purchase')
    customer1.buyBike(store, 'isael')
    print('customer2 purchase')
    customer2.buyBike(store, 'isael4')
    
    print('profit for the store')
    store.checkProfit()