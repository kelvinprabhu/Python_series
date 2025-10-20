# inheritance - It is a way to form new classes using classes that have already been defined.
# The newly formed classes are called derived classes, the classes that we derive from are called base classes.
# Benefits of inheritance: code reusability and method overriding.
# single inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def bark(self):
        return "Dog barks"
d = Dog()
print(d.speak())  # inherited method
print(d.bark())   # own method
# multilevel inheritance
class Puppy(Dog):
    def weep(self):
        return "Puppy weeps"
p = Puppy()
print(p.speak())  # inherited from Animal
print(p.bark())   # inherited from Dog
print(p.weep())   # own method
# use of super() function
class Cat(Animal):
    def speak(self):
        parent_speak = super().speak()  # calling parent class method
        return parent_speak + " and Cat meows"
c = Cat()
print(c.speak())  # overridden method
# multiple inheritance
class Bird:
    def fly(self):
        return "Bird flies"
class Bat(Animal, Bird):
    def fly(self):
        return "Bat flies"
b = Bat()
print(b.speak())  # inherited from
print(b.fly())    # own method
# hierarchical inheritance
class Lion(Animal):
    def roar(self):
        return "Lion roars"
class Tiger(Animal):
    def growl(self):
        return "Tiger growls"
l = Lion()
t = Tiger()
print(l.speak())  # inherited from Animal
print(l.roar())   # own method
print(t.speak())  # inherited from Animal
print(t.growl())  # own method
# hybrid inheritance - combination of two or more types of inheritance
class Father:
    def skills(self):
        return "Gardening, Programming"
class Mother:
    def skills(self):
        return "Cooking, Art"
class Child(Father, Mother):
    def skills(self):
        father_skills = super().skills()  # calls Father's skills due to MRO
        mother_skills = Mother.skills(self)  # explicitly calling Mother's skills
        return father_skills + ", " + mother_skills
ch = Child()
print(ch.skills())  # combined skills
# method resolution order (MRO) - order in which base classes are searched when executing a method
print(Child.mro())  # shows the MRO for Child class

# is instance and is subclass
print(isinstance(d, Dog))        # True
print(isinstance(d, Animal))     # True
print(isinstance(p, Puppy))      # True
print(isinstance(p, Dog))        # True
print(isinstance(c, Cat))        # True
print(isinstance(b, Bat))        # True
print(isinstance(l, Lion))       # True
print(isinstance(t, Tiger))      # True
print(issubclass(Dog, Animal))   # True
print(issubclass(Puppy, Dog))    # True
print(issubclass(Cat, Animal))    # True
print(issubclass(Bat, Bird))     # True
print(issubclass(Lion, Animal))  # True
print(issubclass(Tiger, Animal)) # True
# private and protected members in inheritance
class Base:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"
class Derived(Base):
    def access_members(self):
        print(self.public)          # accessible
        print(self._protected)      # accessible
        # print(self.__private)     # not accessible, will raise AttributeError
d = Derived()
d.access_members()
print(d.public)          # accessible
print(d._protected)      # accessible
# print(d.__private)     # not accessible, will raise AttributeError

# To access private member, we can use name mangling
print(d._Base__private)  # accessible using name mangling
# diamond problem in inheritance - occurs when two classes B and C inherit from A, and class D inherits from both B and C.
class A:
    def show(self):
        return "A's show"
class B(A):
    def show(self):
        return "B's show"
class C(A):
    def show(self):
        return "C's show"
class D(B, C):
    def show(self):
        return "D's show"
d = D()
print(d.show())          # D's show
print(D.mro())          # shows the MRO for D class
# using super() in diamond problem
# class E(B, C):
#     def show(self):
#         return super().show()  # follows MRO
# e = E()
# print(e.show())          # B's show
# print(E.mro())          # shows the MRO for E class