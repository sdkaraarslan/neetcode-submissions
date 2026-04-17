class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.tail.prev == self.head

    def append(self, value: int) -> None:
        newNode = Node(value)
        tailBefore = self.tail.prev

        newNode.next = self.tail
        newNode.prev = tailBefore
        self.tail.prev = newNode
        tailBefore.next = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        headBefore = self.head.next

        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode
        headBefore.prev = newNode

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1
        tailBefore = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return tailBefore.val

    def popleft(self) -> int:
        if self.tail.prev == self.head:
            return -1
        headBefore = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return headBefore.val
        
