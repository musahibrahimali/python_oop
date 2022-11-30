from bank_account import BankAccount
# pip [anaconda -> (conda)] install dataclasses
from dataclasses import dataclass, astuple, asdict

# OOP
# - Inheritance
# - Polymorphism
# - Encapsulation
# - Abstraction

# abstraction (Data Abstraction)
# - hiding the implementation details


my_account = BankAccount("John", 1000)
my_account.deposit(100)
my_account.withdraw(200)
my_account.set_name("Tobit Amofa")
print(my_account.accountNumber)


# PolyMorphism (Poly -> Many, Morph -> Forms)

class English:
    def __init__(self):
        pass

    def say_hello(self):
        print("Hello")


class Italian:
    def __init__(self):
        pass

    def say_hello(self):
        print("Ciao")


class Spanish:
    def __init__(self):
        pass

    def say_hello(self):
        print("Hola")


class Language:
    def __init__(self, language):
        self.language = language

    def say_hello(self):
        self.language.say_hello()


translator = Language(Spanish())

translator.say_hello()


@dataclass
class Comment:
    id: int
    text: str
    author: str
    likes: int = 0
    shares: int = 0
    dislikes: int = 0

    def like(self):
        self.likes += 1

    def share(self):
        self.shares += 1

    def dislike(self):
        self.dislikes += 1


comment = Comment(1, "This is a comment", "Tobit Amofa")
print(astuple(comment))
print(asdict(comment))

