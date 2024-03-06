# print binary tree out of parent array

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def buildBinaryTree(parent,d):
    root=None
    for i in range(len(parent)):
        d[i]=Tree(i)

    for i,e in enumerate(parent):
        if e==-1:
            root=d[i]
        else:
            node=d[e]
            if node.left:
                node.right=d[i]
            else:
                node.left=d[i]
    return root

def inorderrecursive(root):
    if not root:
        return
    inorderrecursive(root.left)
    print(root.data)
    inorderrecursive(root.right)

parent=[-1, 0, 0, 1, 2, 2, 4, 4]
d={}
root=buildBinaryTree(parent,d)
inorderrecursive(root)