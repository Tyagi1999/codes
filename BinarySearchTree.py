class Node():
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

class BinarySearchTree():
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data<node.data:
            if node.leftchild:
                self.insertNode(data,node.leftchild)
            else:
                node.leftchild=Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild=Node(data)

    def removeNode(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.leftchild=self.removeNode(data,node.leftchild)
        elif data>node.data:
            node.rightchild=self.removeNode(data,node.rightchild)
        else:
            if not node.leftchild and not node.rightchild:
                print("removing leaf node...")
                del node
                return None
            if not self.leftchild:
                print("removing a node with single right child...")
                tempNode=node.rightchild
                del node
                return tempnode
            elif not self.rightchild:
                print("removing a node with single left child...")
                tempNode=node.leftchild
                del Node
                return tempNode
            print("removing a node with two children...")
            tempNode=self.getPredecessor(node.leftchild)
            node.data=tempNode.data
            node.leftchild=self.removeNode(tempNode.data,node.leftchild)
        return node    

    def getPredecessor(self,node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        return node

    def remove(self,data):
        if self.root:
            self.root=self.removeNode(data,self.root)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):
        if node.leftchild:
            return self.getMin(node.leftchild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):
        if node.leftchild:
            self.traverseInOrder(node.leftchild)
        print("%s" %node.data)
        if node.rightchild:
            self.traverseInOrder(node.rightchild)

bst=BinarySearchTree()

print("inserting.......")
bst.insert(10)
bst.insert(8)
bst.insert(34)
bst.insert(76)
print("removing.......")
bst.remove(8)
print("traversing.......")
bst.traverse()


