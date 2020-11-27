import math

class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f'x = {self.x}, y = {self.y}')

    def distance(self, inny_obiekt):
        x_dist = (self.x - inny_obiekt.x) ** 2
        y_dist = (self.y - inny_obiekt.y) ** 2
        result = (x_dist + y_dist) ** 0.5
        return result

    def __str__(self):
        return f'Figura koloru {self.color} o środku w punkcie (x, y) {self.x} {self.y}'

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def area(self):
        pole = math.pi * self.radius ** 2
        return pole

    def parimeter(self):
        obwod = 2 * math.pi * self.radius
        return obwod

kolo = Circle(0, 0, 'blue', 10)
k2 = Circle(5, 5, 'red', 1)
print(kolo.area())
print(k2.area())


