class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print(f"Nazywam się {self.name}")
        print(f"Mój e-mail to {self.email}")


u = User("Brajanusz", "brajanusz@mail.com")
u.print_info()