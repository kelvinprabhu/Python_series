# Lambda Functions in Python
""" Lambda functions are anonymous functions defined using the lambda keyword.
    They can have any number of arguments but only one expression. - x
    The expression is evaluated and returned.
    Lambda functions are often used for short, throwaway functions
    where using a full function definition would be syntactically cumbersome.
"""
# Syntax: lambda arguments: expression
# Example 1: A simple lambda function that adds 10 to the input argument
add_10 = lambda x:x + 10
print(add_10(5))  # Output: 15
# Example 2: A lambda function that multiplies two arguments
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6
# Example 3: A lambda function with no arguments that returns a constant value
constant = lambda: 42
print(constant())  # Output: 42
# Example 4: Using lambda functions with built-in functions like map(), filter(), and reduce
# Using lambda with map() to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
# using lambda with sorted() to sort a list of tuples based on the second element
tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_tuples = sorted(tuples, key=lambda x: x[0] + len(x[1]))
print(sorted_tuples)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
# Using lambda with filter() to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# Using lambda with reduce() to compute the product of all numbers in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
