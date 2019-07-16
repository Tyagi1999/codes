class Node(object):
    def __init__(self,val=None,left=None,right=None,is_unival=False):
        self.val=val
        self.left=left
        self.right=right
        self.is_unival=is_unival

def count_unival(node):
    if node.left==node.right==None:
        node.is_unival=True
        return 1
    left=right=0
    if node.left!=None:
        left=count_unival(node.left)
    if node.right!=None:
        right=count_unival(node.right)

    if node.left and node.right:
        if (node.left.is_unival and node.right.is_unival
            and node.val==node.left.val==node.right.val):
            node.is_unival=True
            return left+right+1
        else:
            return left+right
    else:
        if ((not node.left and node.val == node.right.val and node.right.is_unival)
            or (not node.right and node.val==node.left.val and node.left.is_unival)):
            node.is_unival=True
            return left+right+1
        else:
            return left+right

def main():
    root=Node('0',Node('1'),Node('0',Node('1',Node('1'),Node('1')),Node('0')))
    print(count_unival(root))

if __name__=='__main__':
    main()
         
