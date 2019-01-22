# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# Binary search tree 18/1/2019

class Node:

    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False
        # because i don't want duplication in this tree
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
            # return true means we did insert correctly

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False



t = Tree()
t.insert(13)
t.insert(75)
t.insert(14)
t.insert(1)
t.insert(103)
print(t.insert(13))
t.insert(5)
t.insert(130)
print(t.find(75))
print("BST ....")