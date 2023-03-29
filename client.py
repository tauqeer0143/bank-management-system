from random import randint


class Client:
    account = {}

    def __init__(self, name, deposit):
        self.account['account_number'] = randint(100000, 999999)
        self.account['name'] = name
        self.account['holdings'] = deposit

    def withdraw(self, amount):
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            print()
            print("The Amount of {} has been debited from your account balance.".format(amount))
            self.balance()
        else:
            print()
            print("Not enough Balance!")
            self.balance()

    def deposit(self, amount):
        self.account['holdings'] += amount
        print()
        print("The Amount of {} has been added to your account balance.".format(amount))
        self.balance()
    def transfer(self, amount):
        self.account['holdings'] += amount
        print()
        print("The Amount of {} has been credited to  your account balance.".format(amount))
        self.balance()
    def balance(self):
        print()
        print("The current account balance is: {} ".format(self.account['holdings']))