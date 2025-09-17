# tuple: ordered ,immutable, allow duplicate values
# tuples created with parentheses 
mytuple = ("max",1,"hello")
# or
mytuple2 = "max",1,"hello"

print(mytuple)
print(mytuple2)

# tuples from list 
list1 = [1,2,3,4,5]
tuple3 = tuple(list1)
print(tuple3)

# retrieve from tuples
print(mytuple[0])
print(mytuple2[1])
print(tuple3[2])
# retrieve with negative indexing
print(mytuple[-1])
print(mytuple2[-2])
print(tuple3[-3])


# mytuple[1] = 2 # TypeError: 'tuple' object does not support item assignment
#   for loop with tuple
for item in mytuple:
    print(item)

# if with tuple
if "max" in mytuple:
    print("Found 'max' in mytuple")
if 1 in mytuple2:
    print("Found 1 in mytuple2")
if 3 in tuple3:
    print("Found 3 in tuple3")


# len function with tuple
print(len(mytuple))

my_tuple = ('A', 'B', 'C')
print(my_tuple.count('A'))

# use index method to find the position of an element
print(my_tuple.index('B'))

#  convert tuple to list
my_list = list(my_tuple)
print(my_list)

# convert back to tuple 
my_list_tuple = tuple(my_list)
print(my_list_tuple)

# reverse a tuple
reversed_tuple = my_tuple[::-1]
print(reversed_tuple) 

# unpacking tuples
a, b, c = my_tuple
print(a)
print(b)
print(c)

#  unpack multiple elements with *
# the starred expression variable will take all the remaining elements
d, *e = my_tuple
print(d)
print(e)


# why tuple is better than list - pros and cons

# Pros:
# 1. Immutability: Tuples cannot be modified after creation, making them hashable and suitable for use as dictionary keys.
# 2. Performance: Tuples are generally faster than lists for iteration and access due to their fixed size.
# 3. Memory Efficiency: Tuples consume less memory than lists, as they have a smaller memory overhead.

# Cons:
# 1. Immutability: While immutability is a benefit, it can also be a limitation if you need to modify the data.
# 2. Less Built-in Functionality: Lists have more built-in methods and functionalities compared to tuples.