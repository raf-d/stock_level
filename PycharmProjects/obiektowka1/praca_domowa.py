import uuid

class Product:
    next_id = 1

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self._id = Product.next_id
        Product.next_id += 1

    # def set_id(self):
    #     self._id = uuid.uuid1()

    @property
    def id(self):
        return self._id


    def get_total_sum(self):
        return self.quantity * self.price

# aaa = Product('banana', 'long and yellow', 4, 5)
# bbb = Product('apple', 'round and red', 2, 3)
# ccc = Product('carrot', 'long and orange', 2.5, 6)
# ddd = Product('tomato', 'round and red', 3, 4)
# print(aaa.get_total_sum())
# print(ddd.get_total_sum())

lst = []
for i in range(100):
    lst.append(Product(f'nazwa={i+1}', 'b', 1, 1))

for product in lst:
    print(product.name, product.id)