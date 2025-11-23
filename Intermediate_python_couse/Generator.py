# Generator in Python is a special type of iterator that allows you to iterate through a sequence of values without storing them all in memory at once. Generators are defined using functions and the `yield` statement. When a generator function is called, it returns a generator object without executing the function's code. Each time the `next()` function is called on the generator object, the function runs until it hits a `yield` statement, which produces a value and pauses the function's state for the next call.
def simple_generator():
    for i in range (1, 10):
        yield i
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3
# You can also use a for loop to iterate through the generator
print("Using for loop to iterate through generator:")
for value in gen:
    print(value) # Output: 4, 5, 6, 7, 8, 9
    print("")
    # print(next(gen))  # Output: 4, 5, 6, 7, 8, 9
# generator defined as normal fuction but used with yeild function instead of return save the sate of the function until its called again .