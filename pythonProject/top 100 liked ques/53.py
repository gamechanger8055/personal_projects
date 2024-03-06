class Tree:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

def postorderrecursive(root):
    if not root:
        return
    postorderrecursive(root.left)
    postorderrecursive(root.right)
    print(root.data)

def postorderiterative(root):
    st=[root]
    op=[]
    while st:
        curr=st.pop()
        op.append(curr.data)
        if curr.left:
            st.append(curr.left)
        if curr.right:
            st.append(curr.right)
    print("iterative",op[::-1])


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.left = Tree(7)
root.right.left.right = Tree(8)
postorderrecursive(root)
postorderiterative(root)
