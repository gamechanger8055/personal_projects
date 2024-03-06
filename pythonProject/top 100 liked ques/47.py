# Check if a linked list is palindrome or not

class Node:
    def __init__(self,data=None,next=None):
        self.val=data
        self.next=next

def checkPalin(left,right):
    if not right:
        return True,left
    val,left=checkPalin(left,right.next)
    result=val and (left.val==right.val)
    left=left.next
    return result,left

keys = [1, 3, 5, 3, 1]

head = None
for i in reversed(range(len(keys))):
    head = Node(keys[i], head)

if checkPalin(head,head)[0]:
    print('The linked list is a palindrome')
else:
    print('The linked list is not a palindrome')