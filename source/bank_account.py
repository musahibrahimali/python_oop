import random
from dataclasses import dataclass, astuple, asdict


class BankAccount:
    def __init__(self, name, balance):
        self.__accountNumber = self.generate_account_number()
        self.__name = name
        self.__balance = balance

    # static method to generate a 12k string account number
    @staticmethod
    def generate_account_number():
        account_number = "".join([str(random.randint(0, 9)) for _ in range(12)])
        return account_number

    @property
    def accountNumber(self):
        return self.__accountNumber

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    # @name.setter
    def set_name(self, name):
        self.__name = name

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __str__(self):
        return f"Account: {self.__name}, Balance: {self.__balance}"


@dataclass
class Bank:
    accountNumber: str
    name: str
    balance: int

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"Account: {self.name}, Balance: {self.balance}"
