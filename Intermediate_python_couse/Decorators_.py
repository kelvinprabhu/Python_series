# Decorators are a powerful feature in Python that allow you to modify the behavior of functions or methods. They are often used for logging, access control, instrumentation, and caching, among other things.
from doctest import debug
import functools # This module provides tools for working with functions and callable objects.
def start_end_decorator(func):
    @functools.wraps(func) # This decorator preserves the original function's metadata (like its name and docstring).
    def wrapper(*args, **kwargs):
        print("Starting the function...")
        result = func(*args, **kwargs)
        print("Function has ended.")
        return result
    return wrapper

@start_end_decorator
def addition(a, b):
    return a + b

print(addition(5, 7))  # This will print the start and end messages along with the result of the addition function.
print(addition.__name__) # This will print 'addition' because the functools.wraps decorator preserves the original function's metadata.

# Commanly used decorators in Python include:
# @staticmethod - Used to define a static method in a class that does not receive an implicit
# @classmethod - Used to define a class method that receives the class as the first argument instead of an instance.
# @property - Used to define a method as a property, allowing you to access it like an attribute.
# @functools.lru_cache - Used to cache the results of function calls to improve performance for expensive or I/O-bound functions.
# @functools.wraps - Used to preserve the metadata of the original function when writing decorators.

def reapeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        @functools.lru_cache(maxsize=None)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@reapeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # This will print "Hello, Alice!" three times.
# nested decorators
print("Nested Decorators Example:")
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper
@debug
@staticmethod
@start_end_decorator
@reapeat(num_times=2)
def say_hello():
    print("Hello!")
say_hello()  # This will print the start message, "Hello!" twice, and then the end message.