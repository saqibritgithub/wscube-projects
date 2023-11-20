class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Added prev pointer to Node

class LinkedList():
    def __init__(self):
        self.head = None

    def push_in_empty(self, newdata):  # Corrected method name
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
        else:
            print("Linked list is not empty")

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def push_at_end(self, newdata):
        newnode = Node(data=newdata)
        if self.head is None:
            self.head = newnode
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = newnode
        newnode.prev = n

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create an object of the LinkedList class
obj = LinkedList()

# Test push methods
obj.push(4)
obj.push(5)
obj.push(6)

print("Before adding at the end:")
obj.printList()

obj.push_at_end(3)
obj.push_at_end(4)

print("After adding at the end:")
obj.printList()

# Test push_in_empty method
obj_empty = LinkedList()
obj_empty.push_in_empty(10)
obj_empty.push_in_empty(20)
print("Linked list with push_in_empty:")
obj_empty.printList()
