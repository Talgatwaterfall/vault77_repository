class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
 
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.item_models = {}
        self.profit = 0

    def item_create(self, Item):
        self.item_models[Item.name] = Item

    def sell(self, Item):
        self.profit = self.profit

class Cart:
    def __init__(self):
        self.in_cart = {}
        self.profit = 0

    def add_cart(self, Warehouse, Item, number):
        if (Item.name in Warehouse.item_models):
            self.in_cart[Item] = number
            for i in range(number):
                Warehouse.sell(Item)

    def sell(self, Item):
        self.in_cart[Item] = self.in_cart[Item] - 1
        self.profit = self.profit + Item.cost

    def display_in_cart(self):
        for i in self.in_cart:
            print(i.name, self.in_cart[i])

    def show_profit(self):
        return self.profit
   
    def show_available_items(self, Customer):
        for i in self.in_cart:
            if Customer.balance >= i.cost:
                print(i.name, (i.cost))

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
   
    def buy(self, Cart, Item):
        if self.balance >= Item.cost:
            Cart.sell(Item)
            self.my_item = Item
            print("{0} приобрел модель {1}".format(self.name, self.my_item.name))
            self.balance = self.balance - (Item.cost)
            print("Потрачено {0}, остаток {1}".format(Item.cost, self.balance))
        else:
            print("Превышен лимит бюджета, товар не доступен для приобретения")
 
if __name__ == '__main__':

    Iphone = Item("Iphone X", 1000)
    Samsung = Item("Samsung Galaxy S9", 900)
    HTC = Item("HTC U11", 800)

    mobile_phones = Warehouse("Mobile phones")
    mobile_phones.item_create(Iphone)
    mobile_phones.item_create(Samsung)
    mobile_phones.item_create(HTC)

    Cart = Cart()
    Cart.add_cart(mobile_phones, Iphone, 4)
    Cart.add_cart(mobile_phones, Samsung, 4)
    Cart.add_cart(mobile_phones, HTC, 3)

    print("")
    print ("Товары добавлены в корзину для продаж: ")
    Cart.display_in_cart()
    print("")
    print("Текущая прибыль составляет:")
    Cart.show_profit()
    print("---------------------------")
    
    assert Cart.show_profit() == 0

    John = Customer("John", 600)
    print("")
    print ("John: доступные товары для покупке в лимите бюджета John:")
    Cart.show_available_items(John)
    print("")
    John.buy(Cart, Iphone)
    print("")
    print("Наличие телефонов:")
    Cart.display_in_cart()
    print("Полученная прибыль:")
    Cart.show_profit()
    print("---------------------------")  

    Tim = Customer("Tim", 900) 
    print("")
    print ("Tim: Доступные товары для покупке в лимите бюджета Tim:")
    Cart.show_available_items(Tim)
    print("")
    Tim.buy(Cart, Samsung)
    print("")
    print("Наличие телефонов:")
    Cart.display_in_cart()
    print("")
    print("Полученная прибыль:")
    Cart.show_profit()
    print("---------------------------")

    Abu = Customer("Abu", 1500)
    print("")
    print ("Abu: Доступные товары для покупке в лимите бюджета Abu:")    
    Cart.show_available_items(Abu)
    print("")
    Abu.buy(Cart, HTC)
    print("")
    print("Наличие телефонов:")
    Cart.display_in_cart()
    print("")
    print("Полученная прибыль:")
    Cart.show_profit()
    print("---------------------------")