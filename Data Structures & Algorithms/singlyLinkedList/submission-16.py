
class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i=0
        while i < index and curr:
            curr = curr.next
            i+=1
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        i=0
        while i < index and curr:
            curr = curr.next
            i+=1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next=curr.next.next
            return True
        return False
            
    def getValues(self) -> List[int]:
        array = []
        curr = self.head.next
        while curr:
            array.append(curr.val)
            curr = curr.next
        return array
        
