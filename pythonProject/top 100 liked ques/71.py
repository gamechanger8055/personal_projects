# Find k’th largest and smallest node in a BST

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def kthSmallest(root,k):
    if not root:
        return
    left=kthSmallest(root.left,k)
    if not left:
        return left
    k-=1
    if k==0:
        return root
    return kthSmallest(root.right,k)

def kthLargest(root,k):
    ct=0
    klargest=None
    while root:
        if not root.right:
            ct+=1
            if ct==k:
                klargest=root.data

