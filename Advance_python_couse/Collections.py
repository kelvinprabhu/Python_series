"""
The collections module in Python provides specialized containers (different from general purpose built-in containers like dict, list, tuple and set). These specialized containers are designed to address specific programming needs efficiently and offer additional functionalities.
Why do we need Collections Module?
Provides specialized container data types beyond built-in types like list, dict and tuple.
Includes efficient alternatives such as deque, Counter, OrderedDict, defaultdict and namedtuple.
Simplifies complex data structure handling with cleaner and faster implementations.
Helps in frequency counting, queue operations and structured records with minimal code.
Ideal for improving performance and code readability in data-heavy applications.
"""
from collections import namedtuple, deque, Counter, OrderedDict, defaultdict
a = namedtuple('a', ['x', 'y'])
b = "aaaaabbbbbccccc"
# counter - counts the occurence of each element in the iterable
mycounter = Counter(b)
print(mycounter)
print(mycounter.most_common(2))

# OrderedDict - maintains the order of insertion
"""An OrderedDict is a dictionary that preserves the order in which keys are inserted. While regular dictionaries do this from Python 3.7+, OrderedDict also offers extra features like moving re-inserted keys to the end making it useful for order-sensitive operations"""
mydict = OrderedDict()
mydict['a'] = 1
mydict['b'] = 2
mydict['c'] = 3
print(mydict)
# mydict['a'] = 4  # re-inserting 'a' moves it to the end
# print(mydict)
print('Before Deleting')
for key, value in mydict.items():
    print(key, value)

mydict.pop('b')
print('After Deleting')
for key, value in mydict.items():
    print(key, value)

mydict['d'] = 4
mydict['b'] = 1
print('After Adding')
for key, value in mydict.items():
    print(key, value)

# defaultdict - provides a default value for non-existent keys
"""A defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The main feature of a defaultdict is that it provides a default value for the key that does not exist. This means that you do not get a KeyError when you try to access or modify a key that is not present in the dictionary."""
# Creating a defaultdict with default value of 0 (int)
d = defaultdict(int) 
L = [1, 2, 3, 4, 2, 4, 1, 2] 

# Counting occurrences of each element in the list
for i in L: 
    d[i] += 1  # No need to check key existence; default is 0

print(d)  # Output: defaultdict(<class 'int'>, {1: 3, 2: 3, 3: 1, 4: 2})

# ChainMap - groups multiple dictionaries into a single view
"""A ChainMap is a class in the collections module that groups multiple dictionaries (or other mappings and sequences) together to create a single, updateable view. It is useful for managing multiple contexts or scopes, such as combining global and local variables."""
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print("chainMap Example:")
print(chain)  
print(chain['a'])

# Accessing values using values()
print(chain.values())

# Accessing keys using keys()
print(chain.keys())
dict3 = {'d': 5}
# Adding a new dictionary to the ChainMap
chain = chain.new_child(dict3)
print("After adding dict3:")
print(chain)


# deque - a double-ended queue that allows fast appends and pops from both ends
"""A deque (double-ended queue) is a data structure from the collections module that allows you to add and remove elements from both ends with approximately O(1) time complexity. It is implemented as a doubly linked list, making it more efficient than a list for certain operations."""
# Creating a deque
d = deque()
# Adding elements to the right end
d.append(1)
d.append(2)
d.append(3)
print("Deque after appending elements to the right:", d)
# Adding elements to the left end
d.appendleft(0)
print("Deque after appending element to the left:", d)
# Removing elements from the right end
d.pop()
print("Deque after popping element from the right:", d)
# Removing elements from the left end
d.popleft()
print("Deque after popping element from the left:", d)
# Rotating the deque
d.rotate(1)
print("Deque after rotating to the right:", d)
d.rotate(-1)
print("Deque after rotating to the left:", d)
# Limiting the size of the deque
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print("Deque with maxlen after adding 3 elements:", d)
d.append(4)
print("Deque after adding 4th element (oldest removed):", d)
# Reversing the deque
d.reverse()
print("Deque after reversing:", d)
# Clearing the deque
d.clear()
print("Deque after clearing:", d)
# namedtuple - factory function for creating tuple subclasses with named fields
"""A namedtuple is a factory function for creating tuple subclasses with named fields. It allows you to access the elements of the tuple using names instead of indices, making the code more readable and self -documenting."""
# Creating a namedtuple class
Point = namedtuple('Point', ['x', 'y'])
# Creating an instance of the namedtuple
p = Point(10, 20)
# Accessing elements using names
print("Namedtuple Point:", p)
print("x:", p.x)
print("y:", p.y)
# Accessing elements using indices
print("x using index:", p[0])
print("y using index:", p[1])
# Unpacking the namedtuple
x, y = p
print("Unpacked x:", x)
print("Unpacked y:", y)
# Converting namedtuple to a dictionary
p_dict = p._asdict()
print("Namedtuple as dictionary:", p_dict)
# Replacing fields in the namedtuple (returns a new instance)
p2 = p._replace(x=30)
print("Original Point:", p)
print("Modified Point:", p2)
# Getting the field names
print("Field names:", Point._fields)
# Creating a new namedtuple
Circle = namedtuple('Circle', ['center', 'radius'])
c = Circle(center=Point(0, 0), radius=5)
print("Namedtuple Circle:", c)
print("Circle center:", c.center)
print("Circle radius:", c.radius)
print("Circle center x:", c.center.x)
print("Circle center y:", c.center.y)
print("Field names of Circle:", Circle._fields)