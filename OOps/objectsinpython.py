# class
class student:
    name = "kelvin"
# objects
s = student()
# print(s.name)  
class car:
    brand = "Toyota"
    model = "Camry"

car = car()
# print(car.brand)
# print(car.model)
# 
    # default constructors
# __init__ function -- 
# constructor ->  __init__(self, name, brand, model): -- it will execute when we create an object or instance of the class or initiated
class master:
    # self parameter is the referece to the current instance of the class and is used to access variables that belong to the class
    def __init__(self, name, brand, model): # --> parameterised constructor
        self.name = name # instance variable or attribute
        self.brand = brand
        self.model = model
        print("object is created")

m = master("John", "Toyota", "Camry")


#  class and instance attributes and methods

#  class.attr
#  instance.attr
# methods ---> function that belongs that objects
#  class.method()
#  instance.method()

#  obj.attr > class.attr

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def walk(self):
        print(f"{self.name} is walking.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")

    @staticmethod  # decorator -- allows us to wrap another function in order to extend the behavior of the wrapped function , without permanently modifying it
    def sleep():
        print("sleeping...")

person1 = person("Alice", 30)
person1.display_info()  
person1.walk()
person1.birthday()
person1.sleep()

# static methods --> methods that belong to the class rather than any object instance (dont use the self parameter)