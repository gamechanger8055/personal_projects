# Construct a binary tree from inorder and preorder traversal

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def buildTree(inorder, preorder):
    if not inorder or not preorder:
        return None
    ind=preorder.pop(0)
    root=Tree(ind)
    index=inorder.index(ind)
    root.left=buildTree(inorder[:index],preorder)
    root.right=buildTree(inorder[index+1:],preorder)
    return root

def inorderrecursive(root):
    if not root:
        return
    inorderrecursive(root.left)
    print(root.data)
    inorderrecursive(root.right)

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(inorder, preorder)
inorderrecursive(root)
