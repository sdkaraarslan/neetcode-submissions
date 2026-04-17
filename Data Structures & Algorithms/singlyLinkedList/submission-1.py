class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return True

        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        """
        short for>>
        deleted = current.next
        connected = deleted.next
        current.next = connected
        """
        if index == self.length - 1:
            self.tail = current
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        current = self.head
        for i in range(self.length):
            result.append(current.value)
            current = current.next
        return result