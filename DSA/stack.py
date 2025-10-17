# stack memory - stores primitive data types and references to objects in heap memory
# stack follows LIFO - last in first out
# applications - function call management, expression evaluation, backtracking algorithms, undo mechanisms in applications
# operations - push, pop, peek, is_empty, size
# stack - structure that follows LIFO principle - top of stack - last element added
# stack can be implemented using linked list that allows dynamic memory allocation and efficient operations
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    def is_empty(self):
        return self.top == None
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

         
        
        