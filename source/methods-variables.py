
# class variables
# class methods
# static methods

class Animal:
    # animals -> class variable
    animals = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.animals.append(self)

    def eat(self):
        print(self.name + " is eating")

    def sleep(self):
        print(self.name + " is sleeping")

    def drink(self):
        print(self.name + " is drinking")

    # return the number of animals
    @classmethod
    def count_animals(cls):
        return len(cls.animals)

    # static method
    @staticmethod
    def info():
        print("This is an Animal class")

    def __str__(self):
        return f"{self.name}"


dog = Animal("Dog", 5)
cat = Animal("Cat", 5)

Animal.info()
# for animal in Animal.animals:
#     print(animal)
