# diameter of binary tree

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def height(root):
    if not root:
        return 0
    return 1+max(height(root.left), height(root.right))

def diameter(root):
    if not root:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    ldiameter=diameter(root.left)
    rdiameter=diameter(root.right)
    return max(1+lheight+rheight, max(ldiameter, rdiameter))


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print(diameter(root))