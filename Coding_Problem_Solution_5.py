
''' asked by Google

    Given the root to a binary tree, implement serialize(root),
     which serializes the tree into a string, and deserialize(s),
    which deserializes the string back into the tree.

    For example, given the following Node class'''
#class Node:
       #def __init__(self, val, left=None, right=None):
           #self.val = val
           #self.left = left
           #self.right = right'''
'''The following test should pass:'''

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left''''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(tree_node):
    preorder_list=preorder_traversal(tree_node)
    return " ".join(str(x) for x in preorder_list)

def preorder_traversal(node):
    tree_list=[]
    if node is not None:
        tree_list.append(node.val)
        tree_list.extend(preorder_traversal(node.left))
        tree_list.extend(preorder_traversal(node.right))
    if node is None:
        tree_list.append("-1")
    return tree_list

def deserialize(tree_string):
    tree_list=tree_string.split(" ")
    tree=rebuild(tree_list)
    return tree

def rebuild(tree_list):
    if len(tree_list)!=0:
        value=tree_list.pop(0)
        if value!="-1":
            node=Node(value)
            node.left=rebuild(tree_list)
            node.right=rebuild(tree_list)
        else:
            node=Node(None)
    return node

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    print(deserialize(serialize(node)).val)
    print(deserialize(serialize(node)).left.val)
    print(deserialize(serialize(node)).left.left.val)
    print(deserialize(serialize(node)).right.val)

if __name__ == '__main__':
    main()
    
