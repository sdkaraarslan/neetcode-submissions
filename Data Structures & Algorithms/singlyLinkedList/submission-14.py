"""
h1t1 h2t2 h3t3
n/a   

N1    N2    N3
val1 val2 val3

is the list ever empty before insertion? >> will affect removal
"""

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i=0
        while current:
            if i==index:
                return current.value
            current = current.next
            i+=1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next= self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail=newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current = self.head
        i=0
        while i<index and current.next:
            i+=1
            current = current.next

        if current and current.next:
            if current.next==self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        answer = []
        while current:
            answer.append(current.value)
            current = current.next
        return answer


