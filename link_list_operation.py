#insertion at beggining
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
#insertion at given node
class linklist():
    def __init__(self):
        self.head=None
    def AfterNode(self,previous,newdata):
        if previous is None:
            print("this is not the part of linklist")
            return
        new_node=Node(newdata)
        new_node.next=previous.next
        previous.next=new_node

