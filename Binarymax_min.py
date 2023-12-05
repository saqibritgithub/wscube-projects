class BST():
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("The smallest node in this tree is :",current.key)
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("The largest node in this tree is :", current.key)


obj=BST(10)
list=[1,2,3,4,5,6,7,8,9]
for l in list:
    obj.insert(l)
obj.preorder()
obj.min_node()
obj.max_node()