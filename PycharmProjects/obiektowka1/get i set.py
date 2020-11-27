import math
class Car:
    def __init__(self, perdkosc, x, y):
        self.predkosc = perdkosc
        self.x = x
        self.y = y
    @property
    def velocity(self):
        return self.predkosc * 0.78
    @velocity.setter
    def velocity(self, velocity):
        self.predkosc = velocity/0.78
c = Car(100, 0, 0)
c.velocity = 10 #ustaw prędkość samochodu na 10 mil/h
print(c.predkosc)
v = c.velocity
print(v)