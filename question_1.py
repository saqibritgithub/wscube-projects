#creating new node
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist():
    def __init__(self):
        self.head=None
    def push(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node
obj=Linklist()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
x=4
temp=obj.head
v=[]
while(temp):
    v.append(temp.data)
    temp=temp.next
if x in v:
    print("yes this is in list")
else:
    print("NO this is not in list")

