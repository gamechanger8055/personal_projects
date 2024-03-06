# bst insertion
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def insertBST(key,root):
    if not root:
        return Tree(key)
    if key<root.data:
        root.left=insertBST(key, root.left)
    else:
        root.right=insertBST(key, root.right)
    return root

def searchBST(key,root):
    if not root:
        return False
    if root.data==key:
        return True
    if key<root.data:
        return searchBST(key, root.left)
    else:
        return searchBST(key, root.right)


def constructBST(keys):
    root=None
    for key in keys:
        root=insertBST(key, root)
    return root

def inorderrecursive(root):
    if not root:
        return
    inorderrecursive(root.left)
    print(root.data)
    inorderrecursive(root.right)

keys = [15, 10, 20, 8, 12, 16, 25]
root = constructBST(keys)
print(searchBST(16,root))
inorderrecursive(root)