print("Podaj pierwszą liczbę (a):")
a = float(input())
print("Podaj drugą liczbę (b):")
b = float(input())

if a > b:
    print("a jest większe!")
elif a < b:
    print("b jest większe!")
else:
    print("Liczby są równe!")