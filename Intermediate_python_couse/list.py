# Lists: ordered , mutable, allow duplicate values
mylist = [1, 2, 3, 4, 5]
print(mylist)
# list allow mixed data types
# list allow duplicate values
# list maintain insertion order
mylist2 = ['3','5','string','apple']
print(mylist2)
# concat list with + operator
newlist = mylist + mylist2
print(newlist)

# list index 0 - n
# list index -1 -> reverse first element 
# list[::-1] - reverce the list

if 'apple' in newlist:
    print("Apple is in the list")

# len to get lenght 
print(len(newlist))

# to insert use -- append
newlist.append('banana')
print(newlist)

# to insert at specific index use -- insert
newlist.insert(1, 'orange')
print(newlist)

# to remove use -- remove
newlist.remove('banana')
print(newlist)

# to return last element use -- pop - also removes
newlist.pop()
print(newlist)

# to sort the list
# sorted(newlist)
print(newlist)

# to reverse the list use -- reverse
newlist.reverse()
print(newlist)

# to get index of element use -- index
print(newlist.index('orange'))

# to count element use -- count
print(newlist.count('orange'))


# to slice the list - [1:3] -- it slice the list from index 1 to 3
print(newlist[1:3])

# to copy the list use -- copy
newlist2 = newlist.copy()
print(newlist2)

# when list1 = list2 is used, both variables point to the same list object in memory.
# Changes made to one list will affect the other.
newlist2 = newlist
newlist2.append('bananacopy')
print(newlist)
print(newlist2)

# to clear all items use -- clear
newlist.clear()
print(newlist)
