#bottom view of tree
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def bottomViewHelper(root,distance, level, d):
    if not root:
        return
    if distance not in d or level>=d[distance][1]:
        d[distance]=[root,level]
    bottomViewHelper(root.left, distance-1,level+1,d)
    bottomViewHelper(root.right, distance+1,level+1,d)
def bottomView(root):
    d={}
    bottomViewHelper(root,0,0,d)
    for key in sorted(d.keys()):
        print(d[key][0].data)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.right = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.left = Tree(7)
root.right.left.right = Tree(8)
bottomView(root)