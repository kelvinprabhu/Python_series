# inheritance
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class college_student(student):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def display(self):
        super().display()
        print(f"Major: {self.major}")

s1 = college_student("Alice", 20, "Computer Science")
# del s1
s1.display()
