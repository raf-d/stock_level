class Car:
    def __init__(self, predkosc, x, y):
        self.predkosc = predkosc
        self.x = x
        self.y = y

    # def get_velocity_in_km(self):
    #     return self.predkosc

    # @property
    # def velocity_in_km(self):
    #     return self.predkosc
    #
    # def get_velocity_in_miles(self):
    #     return self.predkosc * 0.78
    #
    # @property
    # def velocity_in_miles(self):
    #     return self.predkosc * 0.78

    @property
    def velocity(self):
        return self.predkosc * 0.78

    @velocity.setter
    def velocity(self, velocity):
        self.predkosc = velocity/0.78


c = Car(100, 0, 0)

c.velocity = 10
print(c.velocity)
v = c.velocity
print(v)
# print(c.get_velocity_in_km())
# print(c.velocity_in_km)
# print(c.get_velocity_in_miles())
# print(c.velocity_in_miles)
# abrakadabra = c.get_velocity_in_km
# print(abrakadabra)
