class Node():
    def __init__(self,data):
        self.data=data
        self.head=next
class linklist():
    def __init__(self):
        self.head=None
    def identical(self,listb):
        a=self.head
        b=listb.head
        while(a!=None and b!=None):
            if(a.data!=b.data):
                return False
            a=a.next
            b=b.next
        return(a==None and b==None)
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
list1=linklist()
list2=linklist()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list2.push(1)
list2.push(2)
list2.push(3)
list2.push(4)
if(list1.identical(list2)==True):
    print("identical")
else:
    print("non identical")