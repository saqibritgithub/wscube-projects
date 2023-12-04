class BST():
    def __init__(self,key):
        self.key=key
        self.rchild=None
        self.lchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
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
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()


root=BST(10)
list=[1,2,3,15,5,6,12]
for i in list:
    root.insert(i)
print("preorder")
root.preorder()
print("inorder")
root.inorder()
