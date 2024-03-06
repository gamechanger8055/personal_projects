# all the ancestors of binary tree

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def lca(root,a):
    if not root:
        return
    if root.data==a:
        return True
    left=lca(root.left,a)
    right=lca(root.right,a)
    if left or right:
        print("ffcerf", root.data)
        return True
    return False


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
print("LCA(4, 5) = ", lca(root, 4))
print("LCA(4, 6) = ", lca(root, 6))
print("LCA(3, 4) = ", lca(root, 5))
print("LCA(2, 4) = ", lca(root, 7))

