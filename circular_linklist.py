class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def insert_at_end(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def insert_between_nodes(self, prevdata, data):
        temp = self.head


        while temp is not None and temp.data != prevdata:
            temp = temp.next


        if temp is None:
            print("Node with value  not found in the linked list.")
            return

        newnode = Node(data)
        newnode.next = temp.next
        temp.next = newnode

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


obj = LinkedList()
obj.push(12)
obj.push(13)
obj.push(14)
obj.push(15)

print("Original Linked List:")
obj.print_list()

obj.insert_between_nodes(13, 2)

print("After adding:")
obj.print_list()
