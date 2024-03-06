# Insert a node to its correct sorted position in a sorted linked list

class Node:
    def __init__(self,data,next=None):
        self.val=data
        self.next=next

def insertLL(head,key):
    #start of node
    ptr = Node(key)
    if not head or head.val>=ptr.val:
        ptr.next=head
        head=ptr
        return head
    tmp=head
    while tmp.next and tmp.next.val<key:
        tmp=tmp.next
    ptr.next=tmp.next
    tmp.next=ptr
    return head


def printList(head):
    ptr = head
    while ptr:
        print(ptr.val, end=' —> ')
        ptr = ptr.next
    print('None')

keys = [2, 4, 6, 8]

# points to the head node of the linked list
head = None

# construct a linked list
for i in reversed(range(len(keys))):
    head = Node(keys[i],head)
printList(head)
head = insertLL(head,5)
head =insertLL(head,9)
head = insertLL(head,1)

# print linked list
printList(head)



