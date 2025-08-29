# @property decorator is used onany method in the class to use the method as property

class Employee:
    def __init__(self,name,bonus,fixed,variable):
        self._name = name
        self._bonus = bonus
        self._fixed = fixed
        self._variable = variable

    @property
    def total_compensation(self):
        return self._fixed + self._variable + self._bonus

emp1 = Employee("John", 5000, 70000, 30000)
print(emp1.total_compensation)  # Accessing the method as a property
emp1._fixed = 80000
print(emp1.total_compensation)