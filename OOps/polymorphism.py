# polymorphism
# - > operator overloading : when the same operator is allowed to have different meaning according to the context
# using operators and dunder functions
#  a + b  -> a.__add__(b)
#  a - b  -> a.__sub__(b)
#  a * b  -> a.__mul__(b)
#  a / b  -> a.__truediv__(b)
#  a // b  -> a.__floordiv__(b)
#  a % b  -> a.__mod__(b)
#  a ** b  -> a.__pow__(b)
#  a == b  -> a.__eq__(b)
#  a != b  -> a.__ne__(b)
#  a < b   -> a.__lt__(b)
#  a > b   -> a.__gt__(b)
#  a <= b  -> a.__le__(b)
#  a >= b  -> a.__ge__(b)

class Vectors:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vectors(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vectors(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vectors(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vectors(self.x / scalar, self.y / scalar)

# - > decorator - > getter and setter -- > @property

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, num2):
        return ComplexNumber(self.real + num2.real, self.imag + num2.imag)
    # def __add__(self, other)
    
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(5, 6)
num3 = num1 + num2  # This will invoke num1.__add__(num2)
print(num1.show())
print(num2.show())

print(num1.__add__(num2).show())
print(num3.show())