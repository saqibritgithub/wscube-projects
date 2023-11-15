#searching element in link list
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist():
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)


        new_node.next = self.head


        self.head = new_node
obj=linklist()
(obj.push(3))
obj.push(4)
obj.push(5)
obj.push(6)
x=5
temp=obj.head
v=[]
while(temp):
    v.append(temp.data)
    temp=temp.next
if x in v:
    print("yes")
else:
    print("No")
#finding length of linklist
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist():
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def get_count(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count
link=linklist()
link.push(2)
link.push(3)
link.push(5)
link.push(7)
print("The length of the linklist is:",link.get_count())