# what is init in python?
# __init__ is a special method in Python classes, known as a constructor.
# It is automatically called when an instance (object) of the class is created.
# The primary purpose of __init__ is to initialize the attributes of the newly created object.
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize name attribute
        self.age = age    # Initialize age attribute
# Creating an instance of Person
p1 = Person("Alice", 30)
print(p1.name)  # Output: Alice
print(p1.age)   # Output: 30
# init.py file is used to mark a directory as a Python package directory.
# When a directory contains an __init__.py file, Python treats the directory as a package, allowing you to import modules from that directory.
# It can also be used to execute package initialization code or set the __all__ variable,