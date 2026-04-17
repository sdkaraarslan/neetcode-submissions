class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        #if out of bounds return -1
        curr = self.head.next
        i = 0
        while curr:
            if i==index:
                return curr.value
            i+=1
            curr= curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        #edge case, we may have not next
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next=Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        #if the index is out of bounds, return false, otherwise return true.

    def getValues(self) -> List[int]:
        curr = self.head.next
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

"""
linked list
Node -> Node -> Node
head node...node tail

Node 
[val, next]
"""