#  abstraction -> hiding the implementation details and showing only the essential features of the object
# encapsulation -> wrapping the data and methods that work on the data within one unit
# inheritance -> acquiring the properties and behaviors of another class
# polymorphism -> the ability to present the same interface for different data types
# class -> blueprint for creating objects
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.is_running = False
        self.fuel_level = 100


    def start(self):
        self.is_running = True # this is abstraction as this will not be visible 
        print(f"The {self.year} {self.brand} {self.model} is starting.")

    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.brand} {self.model} is stopping.")

    def accelerate(self):
        if self.is_running:
            self.speed += 10
            self.fuel_level -= 5
            print(f"The {self.year} {self.brand} {self.model} is accelerating.")
        else:
            print(f"The {self.year} {self.brand} {self.model} is not running.")

    def brake(self):
        if self.is_running:
            self.speed -= 10
            print(f"The {self.year} {self.brand} {self.model} is braking.")
        else:

            print(f"The {self.year} {self.brand} {self.model} is not running.")


# Car1 = Car("Toyota", "Camry", 2020)
# Car1.start()
# wait = input("Press Enter to accelerate...")

# Car1.accelerate()

# Car1.brake()

# Car1.stop()
#  encapsulation -> private attributes and methods
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.get_balance()}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.get_balance()}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self): # private methods 
        return self.__balance
Account1 = Account("123456789", "John Doe", 1000)
Account1.deposit(500)
Account1.withdraw(200)
print(f"Account balance is {Account1.get_balance()}.")
