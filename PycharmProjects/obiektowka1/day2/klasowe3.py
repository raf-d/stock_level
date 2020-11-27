import datetime

class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)


    @classmethod
    def create_person(cls, name, year_of_birth):
        current_year = datetime.datetime.today().year
        age = current_year - year_of_birth
        return cls(name, age)

a = Person.create_person('Olo', 2000)
print(a)
