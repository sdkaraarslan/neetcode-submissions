"""
every self connected to Nodes are initiliazed as None.
don't forget next and length while creating a linked list.
for append and prepend, create a new node to work with.
"""

class Node:
    def __init__(self, value):
        self.value = value # stores the value of the node
        self.next = None


# will initialize an empty linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 # stores the number of nodes in the list
    
    # will return the value of the ith node,
    # if the index is out of bounds, return -1
    def get(self, index: int) -> int:
        if index <0 or self.length<=index:
            return -1
        current = self.head
        i=0
        while i<index:
            current = current.next
            i+=1
        return current.value
        """
        for _ in range(index):
            current = current.next
        return current.value
        """

    # will insert a node with val at the head of the list
    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1

    # will insert a node with val at the tail of the list
    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1

    # will remove the ith node (0-indexed)
    # if the index is out of bounds, return false, otherwise return true
    def remove(self, index: int) -> bool:
        if index <0 or self.length <= index:
            return False

        if index == 0:
            self.head = self.head.next
            self.length -=1
            if self.length==0:
                self.tail =None
            return True
            
       # find node before the one to remove
        current = self.head
        for _ in range(index - 1):
            current = current.next

        # remove node
        current.next = current.next.next

        # update tail if last node was removed
        if index == self.length - 1:
            self.tail = current

        self.length -=1
        return True

    # return an array of all the values in the linked list, ordered from head to tail
    def getValues(self) -> List[int]:
        result = []
        current = self.head
        for i in range(self.length):
            result.append(current.value)
            current = current.next
        return result
