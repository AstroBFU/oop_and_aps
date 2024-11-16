import random

class Supplier:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = ['BTC', 'ETH', 'TETHER_USDT']

    def add_product(self, product):
        self.products.append(product)

    def get_info(self):
        return f'Supplier Name: {self.name}, Location: {self.location}, Products: {self.products}'
    
class Customer:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.orders = []

    def buy_order(self, order):
        self.orders.append(order)

    def get_info(self):
        return f'Customer Name: {self.name}, Address: {self.address}, Orders: {self.orders}'
    
class VPN:
    def __init__(self):
        self.suppliers_info = []
        self.customers_info = []

    def hide(self):
        address = ['RUSSIA, MOSCOW', 'FRANCE, PARIS', 'USA, Los Angeles']
        return random.choice(address)
    def get_location(self):
        print("ДАННЫХ НЕ НАЙДЕНО!")


if __name__ == "__main__":
    vpn = VPN()
    supplier1 = Supplier('Supplier ER', location=vpn.hide())
    customer = Customer('Supplier KTX', address='Moscow, Moscow City, tower 1')
    customer.buy_order(supplier1.products[2])

    print(supplier1.get_info())
    print(customer.get_info())

