class BST():
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def delete(self, data):
        if self.key is None:
            print("Node is not present")
            return None

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not present")
        else:
            if self.lchild is None:
                return self.rchild
            elif self.rchild is None:
                return self.lchild
            temp = self.rchild
            while temp.lchild:
                temp = temp.lchild

            self.key = temp.key

            self.rchild = self.rchild.delete(temp.key)

        return self

obj = BST(10)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list:
    obj.insert(i)
obj.preorder()

obj.delete(5)
print("after")
obj.preorder()
