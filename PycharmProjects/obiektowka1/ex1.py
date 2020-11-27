class Lightsaber:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        if self._color == 'czerwony':
            moc = 'ciemna'
        else:
            moc = 'jasna'
        return f'Lightsaber: {self._color}, force: {moc}'

L1 = Lightsaber('czerwony')
print(L1)
L2 = Lightsaber('zielony')
print(L2)