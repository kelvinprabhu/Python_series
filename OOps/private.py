class student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.__roll_number = roll_number

    def __display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.__roll_number}")

    def show(self):
        self.__display()

# private - conceptual implementation in python
# meant to be used within the class and are not accessible from outside the class
# done with __ in front of the variable/attribute name or with front of the methods
# for internal use 
s1 = student("Alice", 20, 101)
# print(s1.__roll_number)
s1.show()
# s1.display()