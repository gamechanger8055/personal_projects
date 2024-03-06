class Tree:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

def levelorderrecursive(root,level):
    if not root:
        return None
    if level==1:
        print(root.data)
    else:
        levelorderrecursive(root.left,level-1)
        levelorderrecursive(root.right,level-1)

def height(root):
    if not root:
        return 0
    return 1+max(height(root.left),height(root.right))

def levelprint(root):
    h=height(root)
    for i in range(1,h+1):
        levelorderrecursive(root,i)

def levelorderiterative(root):
    st=[root]
    while st:
        curr=st.pop(0)
        print("iterative",curr.data)
        if curr.left:
            st.append(curr.left)
        if curr.right:
            st.append(curr.right)
    #print("iterative",op[::-1])


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.left = Tree(7)
root.right.left.right = Tree(8)
levelprint(root)
levelorderiterative(root)
