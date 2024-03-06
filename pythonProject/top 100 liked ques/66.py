# Check if a binary tree is a complete binary tree or not

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def checkByLevelTraversal(root):
    if not root:
        return True
    st=[root]
    flag=False
    while st:
        curr=st.pop(0)
        if flag and (curr.left or curr.right):
            return False
        if not curr.left and curr.right:
            return False
        if curr.left:
            st.append(curr.left)
        else:
            flag=True
        if curr.right:
            st.append(curr.right)
        else:
            flag=True
    return True

def treesize(root):
    if not root:
        return 0
    return 1+treesize(root.left)+treesize(root.right)

def checkbyArrayComputation(root,i,n):
    if not root:
        return True
    if (root.left and 2*i+1>=n) or not checkbyArrayComputation(root.left,2*i+1,n):
        return False
    if (root.left and 2*i+2>=n) or not checkbyArrayComputation(root.left,2*i+2,n):
        return False
    return True


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)

if checkbyArrayComputation(root, 0, treesize(root)):
    print('Complete binary tree')
else:
    print('Not a complete binary tree')


