class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1

        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.value
            i += 1
            current = current.next
        return -1
        
    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next=newNode
        # if list was empty before insertion>>
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head

        while index>i and current:
            i+=1
            current = current.next

        if current and current.next:
            #special case
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        current = self.head.next
        while current:
            ans.append(current.value)
            current = current.next
        return ans

