class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        #linked list init
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        #return ith node\
        if index < 0 or index >= self.length:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def insertHead(self, val: int) -> None:
        #insert a node, with val to head 
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length +=1

    def insertTail(self, val: int) -> None:
        #insert a node, with val to tail 
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length +=1

    def remove(self, index: int) -> bool:
        #remove the ith node
        if index < 0 or index >= self.length:
            return False

        #first node removal
        if index == 0:
            self.head = self.head.next
            self.length -=1
            if self.length == 0:
                self.tail = None
            return True

        #mid node removal
        current = self.head
        for _ in range(index-1):
            current = current.next
        current.next = current.next.next

        #end node removal
        if index == self.length-1:
            self.tail = current
        self.length -=1
        return True

    def getValues(self) -> List[int]:
        #return an array of all the values in the linked list, ordered from head to tail
        values = []
        current = self.head
        for _ in range(self.length):
            values.append(current.value)
            current = current.next
        return values