# ternary operator - It is a one-liner replacement for if-else statement used to assign a value to a variable based on a condition.
# syntax: value_if_true if condition else value_if_false
a = 10
b = 20
max_value = a if a > b else b
print("Max value :",max_value)
min_value = a if a < b else b
print("Min value :",min_value)
# nested ternary operator
x = 5
y = 10
min_value = x if x < y else (y if y < 15 else 15)
print("Min value using nested ternary operator :",min_value)