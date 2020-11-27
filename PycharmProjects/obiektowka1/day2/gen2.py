
tekst = """Wlazł kotek na płotek
i mruga,
ładna to piosenka,
nie długa.
Nie długa, nie krótka,
lecz w sam raz,
zaśpiewaj koteczku,
jeszcze raz.
"""


def sing(text):
    for x in tekst.split('\n'):
        yield(x)

for line in sing(tekst):
    print(line)