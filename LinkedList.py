class Node():
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0

    def insertstart(self,data):
        self.size=self.size+1
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def size1(self):
        return self.size
    
    def size2(self):
        actualNode=self.head
        size=0
        while actualNode is not None:
            size=size+1
            actualNode=actualNode.nextNode
        return size

    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        actualNode=self.head
        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode
        actualNode.nextNode=newNode

    def traverseList(self):
        actualNode=self.head
        while actualNode is not None:
            print("%d" %actualNode.data)
            actualNode=actualNode.nextNode

    def remove(self,data):
        if self.head is None:
            return
        self.size=self.size-1
        currentNode=self.head
        previousNode=None
        while currentNode.data!=data:
            previousNode=currentNode
            currentNode=currentNode.nextNode
        if previousNode is None:
            self.head=currentNode.nextNode
        else:
            previousNode.nextNode=currentNode.nextNode

linkedlist=LinkedList()
print("inserting.....")
linkedlist.insertstart(12)
linkedlist.insertstart(122)
linkedlist.insertstart(3)
linkedlist.insertEnd(34)

print("Size is: ",linkedlist.size1())

print("traversing.....")
linkedlist.traverseList()

print("deleting.....")
linkedlist.remove(3)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(34)

print("Size is: ",linkedlist.size1())
