# asked by Dropbox

# Given the root to a binary search tree, find the second largest node in the tree.



class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def secondLargestUtil(root,c):
    if root==None or c[0]>=2:
        return
    secondLargestUtil(root.right,c)
    c[0]+=1
    if c[0]==2:
        print("2nd largest element is",root.key)
        return
    secondLargestUtil(root.left,c)

def secondLargest(root):
    c=[0]
    secondLargestUtil(root,c)

def insert(node,key):
    if node==None:
        return Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    elif key > node.key:
        node.right=insert(node.right,key)

    return node

if __name__=="__main__":
    root=None
    root=insert(root,50)
    insert(root,30)
    insert(root,20)
    insert(root,40)
    
    insert(root,60)
    insert(root,80)

    secondLargest(root)
    
