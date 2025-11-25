class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "EmptyList"


class CircularLinkedList(LinkedList):
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            if self.head.next == self.head:  # Only one node
                self.head = None
                return True
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return True
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def to_list(self):
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def __repr__(self):
        values = []
        if not self.head:
            return "EmptyCircularList"
        current = self.head
        while True:
            values.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(values) + " (circular)"
    
class DoublyNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

    def __repr__(self):
        return f"DoublyNode({self.data})"
class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return True
        current = self.head
        while current:
            if current.data == data:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                return True
            current = current.next
        return False