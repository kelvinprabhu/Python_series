# Errors and Exception in Python

"""Syntax Errors in Python
Syntax error occurs when the code doesn't follow Python's rules, like using incorrect grammar in English. Python stops and points out the issue before running the program.

Example 1 : In this example, this code returns a syntax error because there is a missing colon (:) after the if statement. The correct syntax requires a colon to indicate the start of the block of code to be executed if the condition is true."""



# ---
# Notes: Types of Errors in Python
# ---

# 1. SyntaxError
# Occurs when Python code is not written correctly according to the language rules.
# Example:
# print("Hello"
# Output: SyntaxError: unexpected EOF while parsing

# 2. IndentationError
# Happens when the code is not properly indented.
# Example:
# if True:
# print("Hello")
# Output: IndentationError: expected an indented block

# 3. NameError
# Raised when a variable or function name is not found.
# Example:
# print(x)
# Output: NameError: name 'x' is not defined

# 4. TypeError
# Occurs when an operation is applied to an object of inappropriate type.
# Example:
# a = 5 + "hello"
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 5. ValueError
# Raised when a function receives an argument of correct type but inappropriate value.
# Example:
# int("abc")
# Output: ValueError: invalid literal for int() with base 10: 'abc'

# 6. IndexError
# Occurs when trying to access an index that is out of range.
# Example:
# lst = [1, 2, 3]
# print(lst[5])
# Output: IndexError: list index out of range

# 7. KeyError
# Raised when a dictionary key is not found.
# Example:
# d = {"a": 1}
# print(d["b"])
# Output: KeyError: 'b'

# 8. AttributeError
# Occurs when an invalid attribute reference is made.
# Example:
# x = 5
# x.append(3)
# Output: AttributeError: 'int' object has no attribute 'append'

# 9. ImportError / ModuleNotFoundError
# Raised when an import fails.
# Example:
# import non_existing_module
# Output: ModuleNotFoundError: No module named 'non_existing_module'

# 10. ZeroDivisionError
# Occurs when dividing by zero.
# Example:
# a = 5 / 0
# Output: ZeroDivisionError: division by zero

# 11. FileNotFoundError
# Raised when a file or directory is requested but doesn’t exist.
# Example:
# open("nofile.txt")
# Output: FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'

# These are the most common error types in Python. There are more built-in exceptions, but these cover the majority of everyday programming scenarios.