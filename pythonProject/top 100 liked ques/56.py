# check if trees are identical

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def checkIdenticalRecursive(x, y):
    if not x and not y:
        return True
    return (x and y) and (x.data == y.data) and checkIdenticalRecursive(x.left,
                                                                                y.left) and checkIdenticalRecursive(
        x.right, y.right)


def checkIdenticalIterative(x, y):
    st=[]
    if not x and not y:
        return True
    if not x:
        return False
    if not y:
        return False

    st.append((x,y))
    while st:
        x,y=st.pop()
        if x.data!=y.data:
            return False
        if x.left and y.left:
            st.append((x.left,y.left))
        elif x.left or y.left:
            return False
        if x.right and y.right:
            st.append((x.right,y.right))
        elif x.right or y.right:
            return False
    return True




x = Tree(15)
x.left = Tree(10)
x.right = Tree(20)
x.left.left = Tree(8)
x.left.right = Tree(12)
x.right.left = Tree(16)
x.right.right = Tree(25)

# construct the second tree
y = Tree(15)
y.left = Tree(10)
y.right = Tree(20)
y.left.left = Tree(8)
y.left.right = Tree(12)
y.right.left = Tree(16)
y.right.right = Tree(25)

if checkIdenticalRecursive(x, y):
    print('The given binary trees are identical')
else:
    print('The given binary trees are not identical')

if checkIdenticalIterative(x, y):
    print('I: The given binary trees are identical')
else:
    print('I: The given binary trees are not identical')
