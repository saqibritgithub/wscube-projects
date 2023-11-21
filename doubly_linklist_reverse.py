class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linklist():
    def __init__(self):
        self.head=None
    def push(self,newdata):
        newnode=Node(data=newdata)
        newnode.next=self.head
        newnode.prev=None
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end="")
            temp=temp.next
        print()
    def reverse(self):
        prev=None
        current=self.head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
            self.head=prev
myobj=Linklist()
myobj.push(2)
myobj.push(3)
myobj.push(4)
myobj.push(5)
myobj.printlist()
myobj.reverse()
print("After reverse :")
myobj.printlist()
