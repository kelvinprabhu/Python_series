class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
# b.next = c
# print(a.data)
# print(a.next.data)
# print(a.next.next.data)
# print(a.next)
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    # length of linked list is number of nodes
    def length(self):
        return self.n
    # insert can be at begining, end or at specific index
    def insert_at_head(self,data):
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node
         self.n += 1
    # head is none when linked list is empty
    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    
    def append(self,value):
        new_node = Node(value)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr_next = new_node
        self.n += 1



L = LinkedList()
L.insert_at_head(1)
L.insert_at_head(2)
L.insert_at_head(3)
L.insert_at_head(4)
# print(L.head.data)
# print(L.head.next.data)
# L.traverse()
print(L) 

print("append")
L.append(4)
print(L.length())

print(L)