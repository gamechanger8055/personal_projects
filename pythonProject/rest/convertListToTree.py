def lltoTree(head):
    if not head:
        root=None
        return
    root=Tree(head.data)
    q=[]
    q.append(root.data)
    temp=head.next
    while temp:
        parent=q.pop(0)
        leftChild=None
        rightChild=None
        if not leftChild:
            leftChild=Tree(temp.data)
            q.append(leftChild)
            temp=temp.next
        if temp and not rightChild:
            rightChild=Tree(temp.data)
            q.append(rightChild)
            temp = temp.next
        parent.left=leftChild
        parent.right=rightChild


def rob(nums):
    if not nums:
        return 0

    def rob_helper(nums):
        prev_max = 0
        curr_max = 0
        for num in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + num)
            prev_max = temp
        return curr_max

    m1 = rob_helper(nums[:-1])
    m2 = rob_helper(nums[1:])
    return max(m1, m2)


print(rob([1, 2, 3, 1]))



