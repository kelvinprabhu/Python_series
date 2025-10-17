# types of memory 
# - stack mem
# - private heap memory 

# stack memory - stores primitive data types and references to objects in heap memory
# heap memory - stores objects and instance variables
# Reference meathod calls are stored in stack memory
x = 10  # primitive data type stored in stack memory
y = 20  # primitive data type stored in stack memory
# value objects 10 and 20 are stored in heap memory
print(type(x))
print(type(y))
# show memory addresses
print(f"Memory address of x: {id(x)}")
print(f"Memory address of y: {id(y)}")
class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable stored in heap memory
        self.age = age    # instance variable stored in heap memory

p1 = Person("Alice", 30)  # object stored 
p2 = Person("Bob", 25)    # object stored in heap memory
# p1 and p2 references stored in stack memory
print(f"p1: {p1.name}, {p1.age}")
print(f"p2: {p2.name}, {p2.age}")
# memory management in python is handled by python memory manager
# memory allocation and deallocation is done automatically using garbage collection   