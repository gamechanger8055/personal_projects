# Build a Binary Search Tree from a preorder sequence

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def buildBSTbyPreOrder(preorder):
    val=preorder.pop(0)
    root=Tree(val)
    i=0
    while preorder[i]<val:
        i+=1
    root.left=buildBSTbyPreOrder(preorder[:i])
    root.right=buildBSTbyPreOrder(preorder[i:])

