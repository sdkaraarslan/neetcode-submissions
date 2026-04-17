class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while i<index and current:
            current = current.next
            i+=1
        if i == index and current:
            return current.val
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
        current = self.head
        i = 0
        while i<index and current.next:
            current = current.next
            i +=1
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        answer = []
        while current:
            answer.append(current.val)
            current = current.next
        return answer

        
