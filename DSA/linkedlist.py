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
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    def search(self,key):
        curr = self.head
        position = 0
        while curr is not None:
            if curr.data == key:
                return position
            curr = curr.next
            position += 1
        return "Not found"

L = LinkedList()
L.insert_at_head(1)
L.append(2)
L.append(3)
L.append(4)
# print(L.head.data)
# print(L.head.next.data)
# L.traverse()
print(L) 

print("append")
L.append(5)
# print(L.length())

print(L)

#  advantages of linked list over array - 
#  1. Dynamic Size: Linked lists can grow and shrink in size by allocating and deallocating memory as needed, unlike arrays which have a fixed size.
#  2. Efficient Insertions/Deletions: Inserting or deleting elements in a linked list is more efficient (O(1) time complexity) compared to arrays (O(n) time complexity) since we don't need to shift elements.
#  3. No Memory Wastage: Linked lists use memory more efficiently as they allocate memory for each element individually, whereas arrays may allocate more memory than needed.