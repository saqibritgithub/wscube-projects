#print node at given index
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkList():
    def __init__(self):
        self.head=None
    def push(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node
    def getindex(self,index):
        current=self.head
        count=0
        while(current):
            if(count==index):
                return current.data
            count+=1
            current=current.next
myobj=LinkList()
myobj.push(1)
myobj.push(2)
myobj.push(3)
myobj.push(4)
myobj.push(5)
n=2
print("The value at 3 index is:",myobj.getindex(n))
