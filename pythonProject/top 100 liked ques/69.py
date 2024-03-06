#bst deletion all cases
# 1. leaf node
# 2. root with one leaf
# 3. root with 2 leaf

def deleteKey(root,key):
    root=searchKey(root,key)
    if root:
        if not root.left and not root.right:
            return None
        elif root.left and root.right:
            pres=findMin(root.left)
            root.data=pres.data
            root.left=deleteKey(root.left,pres.data)
        else:
            child=root.left if root.left else root.right
            root=child
    return root