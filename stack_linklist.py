class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack():
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top is None:
            print("the stack is empty")
            return
        popped_data=self.top
        self.top=self.top.next
        return popped_data
    def peak(self):
        if  self.top is None:
            print("stack is empty")
            return
        return self.top.data
    def printstack(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
stack=Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.printstack()
stack.pop()
print("After popping")
stack.printstack()

