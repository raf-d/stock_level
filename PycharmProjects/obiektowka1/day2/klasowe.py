class Calculator:

    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        add = num1 + num2
        self.history.append(f'added {num1} to {num2} got {add}')
        return add

    def multiply(self, num1, num2):
        multiply = num1 * num2
        self.history.append(f'multiplied {num1} with {num2} got {multiply}')
        return multiply

    def print_operations(self):
        for i in self.history:
            print(i)

class AdvancedCalculator(Calculator):
    PI = 3.14159265

    @staticmethod
    def compute_circle_area(r):
        return AdvancedCalculator.PI * r ** 2

print((AdvancedCalculator.compute_circle_area(10)))
a = AdvancedCalculator()
print(a.compute_circle_area(15))

# k1 = Calculator()
# print(k1.add(1, 2))
# print(k1.multiply(3, 4))
# k1.print_operations()
