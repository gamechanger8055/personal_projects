# sort a linked list
class Node:
    def __init__(self,data=None,next=None):
        self.val=data
        self.next=next

def insertLL(head,key):
    #start of node
    ptr=Node(key)
    dummy=Node()
    tmp=dummy
    dummy.next=head
    while tmp.next and tmp.next.val<key:
        tmp=tmp.next
    ptr.next=tmp.next
    tmp.next=ptr
    return dummy.next

def insertSort(head):
    temp=head
    result=None
    while temp:
        next=temp.next
        result=insertLL(result,temp.val)
        temp=next
    return result
def printList(head):
    ptr = head
    while ptr:
        print(ptr.val, end=' —> ')
        ptr = ptr.next
    print('None')

keys = [6, 3, 4, 8, 2, 9]

# points to the head node of the linked list
head = None

# construct a linked list
for i in reversed(range(len(keys))):
    head = Node(keys[i],head)
printList(head)
head = insertSort(head)

# print linked list
printList(head)



