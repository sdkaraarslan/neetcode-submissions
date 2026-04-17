'''
Node {value,next}

Node1 Node2 Node3 Node4
head.   n.    n.   tail
dummy node 
'''

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
            i+=1
            current = current.next
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
        while i<index and current:
            i+=1
            current = current.next

        if current and current.next:
            if current.next==self.tail:
                self.tail=current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        answer = []
        while current:
            answer.append(current.value)
            current=current.next
        return answer


        
