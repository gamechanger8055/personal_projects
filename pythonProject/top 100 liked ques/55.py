# spiral order traversal(later)

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

def spirallevelorderiterative(root):
    st=[root]
    m=[]
    ctr=0
    while st:
        #for i in range(len(st)):
        curr=st.pop(0)
        print("iterative",curr.data)
        if ctr%2==0:
            if curr.left:
                st.append(curr.left)
                m.append(curr.left.data)
            if curr.right:
                st.append(curr.right)
                m.append(curr.right.data)
        else:
            if curr.right:
                st.append(curr.right)
                m.append(curr.right.data)

            if curr.left:
                st.append(curr.left)
                m.append(curr.left.data)
        ctr+=1
        #m.append(curr)
        #ctr+=1
        #m=m[::-1]

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.left = Tree(7)
root.right.left.right = Tree(8)
spirallevelorderiterative(root)