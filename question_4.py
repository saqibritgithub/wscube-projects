#moving last node to front
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def move_to_front(self):
        if not self.head or not self.head.next:
            return

        last = self.head
        while last.next.next:
            last = last.next

        last.next.next = self.head
        self.head = last.next
        last.next = None

    def display_data(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
my_obj = LinkedList()
my_obj.push(2)
my_obj.push(4)
my_obj.push(5)
my_obj.push(6)
my_obj.push(7)

print("Original linked list:")
my_obj.display_data()

my_obj.move_to_front()

print("Linked list after changing:")
my_obj.display_data()
