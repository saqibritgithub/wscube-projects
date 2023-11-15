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
    def get_count(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count
obj=Linklist()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
print("The length of linklist is ",obj.get_count())
