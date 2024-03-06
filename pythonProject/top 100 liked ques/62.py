# lowest common ancestor(LCA) of binary tree

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def lca(root,a,b):
    if not root:
        return
    if root.data==a or root.data==b:
        return root
    left=lca(root.left,a,b)
    right=lca(root.right,a,b)
    if left and right:
        return root
    return left if left else right


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
print("LCA(4, 5) = ", lca(root, 4, 5).data)
print("LCA(4, 6) = ", lca(root, 4, 6).data)
print("LCA(3, 4) = ", lca(root, 3, 4).data)
print("LCA(2, 4) = ", lca(root, 2, 4).data)

