def fibb(n):
    n -= 2
    x0 = 1
    x1 = 1
    yield x0
    yield x1
    while n > 0:
        wynik = x0 + x1
        yield wynik
        x0 = x1
        x1 = wynik
        n -= 1

for x in fibb(5):
    print(x)