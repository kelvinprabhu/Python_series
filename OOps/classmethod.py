# class methods







class Person:
    name = "John"
    age = 30

    def change_name(self, new_name):
        self.name = new_name
        # Person.name = "changed"

    @classmethod
    def display_info(cls):
        print(f"Name: {cls.name}, Age: {cls.age}")

# Person.display_info()
p1 = Person()
p1.change_name("Alice")
print(p1.name)  # Output: Alice
print(Person.name)  # Output: John
p1.display_info() # Output: Name: John, Age: 30

# class method is bound to the class and recieves the class as an implicit first argument

# note static method is a method that is bound to the class and not the object of the class