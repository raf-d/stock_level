class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def przedstaw_sie(self):
        print(f'nazywam sie {self.first_name} {self.last_name}')


class Client(Person):
    pass

p = Person('Ala', 'Makota')
print(type(p))
c = Client('Sławek', 'Bogusł')
print(type(c))
p.przedstaw_sie()
c.przedstaw_sie()