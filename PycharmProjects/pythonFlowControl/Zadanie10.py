print("Tabliczka mnożenia, podaj liczbę z przedziału 1-10:")
num = int(input())

for i in range(1, 11):
    num1 = i * num
    print(f"{i} * {num} = {num1}")
