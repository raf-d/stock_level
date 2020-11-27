print("Podaj ile liczb chcesz wprowadzić:")
n = int(input())
numbers = []
for i in range(n):
    print(f"Wprowadź {i + 1}. liczbę")
    num = int(input())
    numbers.append(num)

suma = sum(numbers)
srednia = suma / n

print(f"Wprowadzone liczby: {numbers}")
print(f"suma: {suma},")
print(f"średnia: {srednia}")

if suma > srednia:
    print("Suma jest większa!")
else:
    print("Średnia jest większa!")
