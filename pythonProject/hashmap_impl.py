class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.next=None

class HashMap:
    def __init__(self,size):
        self.size=size
        self.buckets=[None]*size

    def hash_mod(self,key):
        return key%self.size

    def put(self,key,value):
        index=self.hash_mod(key)
        if index not in self.buckets:
            self.buckets[index]=ListNode(key,value)
        else:
            curr=self.buckets[index]
            while curr:
                if curr.key==key:
                    curr.val=value
                    return
                curr=curr.next
            curr.next=ListNode(key,value)

    def get(self,key):
        index = self.hash_mod(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.val
        return -1

    def remove(self,key):
        index = self.hash_mod(key)
        curr=prev=self.buckets[index]
        if not curr:
            return
        if curr.key==key:
            self.buckets[index]=curr.next
        curr=curr.next
        while curr:
            if curr.key==key:
                prev.next=curr.next
                return
            curr=curr.next
            prev=prev.next

hash_map = HashMap(500)
hash_map.put(1, "Hello")
hash_map.put(2, "World")
print(hash_map.get(1))  # Output: "Hello"
print(hash_map.get(3))  # Output: -1
hash_map.put(2, "Python")
print(hash_map.get(2))  # Output: "Python"
hash_map.remove(2)
print(hash_map.get(2))  # Output: -1