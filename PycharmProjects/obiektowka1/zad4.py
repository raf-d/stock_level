class Employee:
    def __init__(self, id, imie, nazwisko, _salary):
        self.id = id
        self.first_name = imie
        self.last_name = nazwisko
        self._salary = _salary

    def set_salary(self, salary):
        if type(salary) == int or type(salary) == float:
            if salary >= 0:
                self._salary = salary

    def set_salary_from_all(self, salary):
        try:
            salary = float(salary)
            if salary >= 0:
                self._salary = salary
        except ValueError:
            pass

class HourlyEmployee(Employee):
    def compute_payment(self, hours):
        return self._salary * hours

class SalariedEmployee(Employee):
    def compute_payment(self):
        return self._salary * 190

p = HourlyEmployee(111, 'Tom', 'Mot', 20)
print(p.compute_payment(160))

p = SalariedEmployee(111, 'Tom', 'Mot', 20)
print(p.compute_payment())

# e = Employee(1, 's', 'b')
# e.set_salary_from_all("1000")
# print(e._salary)

