#print middle of linklist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        new_node = Node(newdata)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle of this linked list is:", slow.data)

myobj = LinkedList()
myobj.push(1)
myobj.push(2)
myobj.push(3)
myobj.push(4)
myobj.push(6)
myobj.print_middle()
