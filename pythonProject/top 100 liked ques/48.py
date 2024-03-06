# Merge two sorted linked lists into one

class Node:
    def __init__(self,data=None,next=None):
        self.val=data
        self.next=next


def printList(msg, head):
    print(msg, end='')
    ptr = head
    while ptr:
        print(ptr.val, end=' —> ')
        ptr = ptr.next
    print('None')

def sortedMerge(a,b):
    dummy=Node()
    temp=dummy
    while True:
        if not a:
            temp.next=b
            break
        elif not b:
            temp.next=a
            break
        elif a.val<=b.val:
            if a:
                newNode=a
                a=a.next
                newNode.next=temp.next
                temp.next=newNode
        elif b:
            newNode = b
            b = b.next
            newNode.next = temp.next
            temp.next = newNode
        temp=temp.next
    return dummy.next


a = b = None
for i in reversed(range(1, 8, 2)):
    a = Node(i, a)

for i in reversed(range(2, 7, 2)):
    b = Node(i, b)

# print both lists
printList('First List: ', a)
printList('Second List: ', b)

head = sortedMerge(a, b)
printList('After Merge: ', head)

