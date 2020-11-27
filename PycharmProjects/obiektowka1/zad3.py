class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount
        return self.cash

    def withdraw_cash(self, amount):
        if amount <= self.cash:
            self.cash -= amount
            return amount
        else:
            return self.cash

    def print_info(self):
        print(f'{self.number} posiada {self.cash}')

konto1 = BankAccount(321321321)
konto1.withdraw_cash(100)
konto1.print_info()
konto1.deposit_cash(1000)
konto1.print_info()