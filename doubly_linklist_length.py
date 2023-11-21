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
    def find_length(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return  count
myobj=Linklist()
myobj.push(1)
myobj.push(2)
myobj.push(3)
myobj.push(4)
print("The length of this linklist is :",myobj.find_length())