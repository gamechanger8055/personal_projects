class Tree:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

def preorderrecursive(root):
    if not root:
        return
    print(root.data)
    preorderrecursive(root.left)
    preorderrecursive(root.right)

def preorderiterative(root):
    st=[root]
    while st:
        curr=st.pop()
        print("iterative", curr.data)
        if curr.right:
            st.append(curr.right)
        if curr.left:
            st.append(curr.left)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.left = Tree(7)
root.right.left.right = Tree(8)
preorderrecursive(root)
preorderiterative(root)
