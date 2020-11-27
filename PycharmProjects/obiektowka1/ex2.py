Sabers = {
    'czerwony': 'Ciemna',
    'niebieski': 'Jasna',
    'zielony': 'Jasna',
    'fioletowy': 'Jasna'
}
class LightSaber:
    def __init__(self, color):
        self.color = color


    def __str__(self):
        return f'Lightsaber: {self._color}, force: {self.force_side}'


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color in Sabers:
            self._color = color
        else:
            raise ValueError('Nie ma takiego miecza')

    @property
    def force_side(self):
        return Sabers[self._color]

L1 = LightSaber('czerwony')
print(L1)
L2 = LightSaber('zielony')
print(L2)