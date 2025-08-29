# inheritance -- when one method is inherited from a parent class by a child class
# - properties and methods of another class - parent 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.father = "baap"
    @staticmethod
    def walk():
        print("Walking on two legs.")

    @staticmethod
    def talk():
        print("Talking in human language.")

    @staticmethod
    def display_info(person):
        person.walk()
        person.talk()
        person.display()

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display(self):
        super().display()
        print(f"Roll Number: {self.roll_number}")

person1 = Student("Alice", 20, "S123")

person1.walk() # inherited method
print(person1.father) # inherited property
class Topperstudent(Student):
    def __init__(self, name, age, roll_number, subject):
        super().__init__(name, age, roll_number)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

topper1 = Topperstudent("Bob", 21, "S124", "Mathematics")
# multilevel inheritance
topper1.walk() # inherited method
print(topper1.father) # inherited property
topper1.display() # overridden method

# super() -- > use to call the parent class methods -- constructor
# In the constructor of Topperstudent, we call the constructor of Student using super().__init__(name, age, roll_number)
# This allows us to initialize the inherited properties from the Student class.

# multiple inheritance -- when a class is derived from more than one base class

class A:
    valA = "Value from A"

class B:
    valB = "Value from B"

class C(A, B):
    valC = "Value from C"
    def add_values(self):
        return self.valA + " " + self.valB + " " + self.valC

c1 = C()
print(c1.add_values())