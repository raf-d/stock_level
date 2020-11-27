print("Wprowadź liczbę, program policzy sumę od wszystkich liczb od 0 do Twojej:")
num = int(input())
num1 = num
num2 = num

for i in range(num1):
    num1 += i
print(num1)

print("Druga wersja programu")
print(sum(range(num2 + 1)))
