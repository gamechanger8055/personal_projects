#right view of tree
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def rightViewHelper(root,distance, level, d):
    if not root:
        return
    if distance not in d or level>=d[distance][1]:
        d[distance]=[root,level]
    rightViewHelper(root.left, distance+1,level+1,d)
    rightViewHelper(root.right, distance+1,level+1,d)
def rightView(root):
    d={}
    rightViewHelper(root,0,0,d)
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
rightView(root)