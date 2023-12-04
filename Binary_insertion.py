class BinarySearchTree():
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
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BinarySearchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BinarySearchTree(data)


root=BinarySearchTree(None)
root.insert(12)
root.insert(10)
root.insert(1)