# Sets in Python
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements after creation.
# However, the elements themselves must be immutable (e.g., numbers, strings, tuples).
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)
# Creating a set using the set() constructor
another_set = set([4, 5, 6, 7, 8])
print("", another_set)
# Adding elements to a set
my_set.add(6)
another_set.add(7)
print("Set after adding elements:", my_set)
print("Another set after adding elements:", another_set)
# Removing elements from a set
my_set.remove(3)  # Raises KeyError if 3 is not found
# set operations
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)
difference_set = my_set.difference(another_set)
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set) # Elements in my_set but not in another_set
print("Symmetric Difference:", symmetric_difference_set) # Elements in either set but not in both
# set comprehension
squared_set = {x**2 for x in range(10)}
print("Squared set:", squared_set)
# Frozenset - immutable version of a set
frozen = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", frozen)
# use case of sets - removing duplicates from a list and membership testing
# membership testing
print("Is 4 in my_set?", 4 in my_set)
print("Is 10 in another_set?", 10 in another_set)

# Removing duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list_no_duplicates = list(set(my_list))
print("List without duplicates:", my_list_no_duplicates)
# get comman elements from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)
print("Common elements between list1 and list2:", common_elements)
