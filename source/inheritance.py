class Person:
    children = []  # number of children

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def walk(self):
        print(f"{self.first_name} is Walking")

    def talk(self):
        print(f"{self.first_name} is Talking")

    def eat(self):
        print(f"{self.first_name} is Eating")

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name} {self.age}"


class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} {self.age} {self.student_id}"

    def __gt__(self, other):
        return self.age > other.age


def main():
    p = Person("John", "Smith", 35)
    # print(p)
    # p.walk()
    # p.talk()
    # p.eat()

    s = Student("Jane", "Doe", 25, 12345)
    print(s)
    # s.walk()
    # s.talk()
    # s.eat()

    # print(s > p)


if __name__ == "__main__":
    main()
