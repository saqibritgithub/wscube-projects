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
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key==data:
            print("The node is present")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("This node is not present")
                return
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("This node is not present")


root=BST(10)
list=[2,3,4,5,6,7,8]
for l in list:
    root.insert(l)
root.search(8)