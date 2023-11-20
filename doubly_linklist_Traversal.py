class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList():
    def __init__(self):
        self.head=None

    def push(self, new_data):
            new_node = Node(data=new_data)
            new_node.next = self.head
            new_node.prev = None
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
    def travelsal(self):
        if self.head is None:
            print("link list is empty")
        else:
            n=self.head
            while(n.next is not None):
                print(n.data,end="")
                n=n.next
            print()

    def reversal_travelsal(self):
        if self.head is None:
            print("linklist is empty")
            return
        else:
            n = self.head
            while (n.next is not None):
                n = n.next
            while n is not None:
                print(n.data,end="")
                n=n.prev
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,data="")
            temp=temp.next
        print()
myobj=LinkedList()
myobj.push(1)
myobj.push(2)
myobj.push(3)
myobj.push(4)
myobj.push(5)
print("forward traversal")
myobj.travelsal()
print("reverse traversal")
myobj.reversal_travelsal()




