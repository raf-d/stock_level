# projekt zrobiony przez Sławka

class Product:
    next_id = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.next_id
        Product.next_id += 1


class ShoppingCart:

    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        if product.id in self.products:
            self.quantities[product.id] += 1
        else:
            self.products[product.id] = product
            self.quantities[product.id] = 1

    def remove_product(self, product):
        if product.id in self.products:
            del self.products[product.id]
            del self.quantities[product.id]


    def change_product_quality(self, product, quantity):
        if product.id in self.products:
            if quantity > 0:
                self.quantities[product] = quantity
            elif quantity == 0:
                self.remove_product(product)
            else:
                raise ValueError('Odpowiedni komentarz')

