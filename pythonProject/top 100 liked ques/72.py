# Find inorder successor for the given key in a BST

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findMin(root):
    while root.left:
        root=root.left
    return root

def successor(root,succ,key):
    if not root:
        return succ
    if root.data==key:
        if root.right:
            return findMin(root.right)
    elif key<root.data:
        succ=root
        return successor(root.left,succ,key)
    else:
        return successor(root.right,succ,key)


for key in keys:
    succ = successor(root, None, key)

    if succ:
        print(f'The successor of node {key} is {succ.data}')
    else:
        print(f'No Successor exists for node {key}')

