class Tree:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

def inorderrecursive(root):
    if not root:
        return
    inorderrecursive(root.left)
    print(root.data)
    inorderrecursive(root.right)

def inorderiterative(root):
    curr=root
    st=[]
    while st or curr:
        if curr:
            st.append(curr)
            curr=curr.left
        else:
            curr=st.pop()
            print("iterative", curr.data)
            curr=curr.right

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.left = Tree(7)
root.right.left.right = Tree(8)
#inorderrecursive(root)
inorderiterative(root)
