class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [None] * self.capacity


    def get(self, i: int) -> int:
        if i<0 or i >= self.length:
            raise IndexError("index out of range")
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        if i<0 or i > self.length:
            raise IndexError("index out of range")
        self.array[i] = n

        
    def insert(self, i: int, n: int) -> None:
        if i<0 or i > self.length:
            raise IndexError("index out of range")
        
        #resize if full
        if self.length == self.capacity:
            self.resize()

        for idx in range(self.length-1, i-1, -1):
            self.array[idx+1] = self.array[idx]
        self.array[i] = n
        self.length += 1


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            raise IndexError("index out of range")
        self.length -=1
        endValue = self.array[self.length]
        return endValue 

    def resize(self) -> None:
        newCapacity = 2 * self.capacity
        newArray = [None] * newCapacity
        
        #copy the element of the old array
        for idx in range(self.length):
            newArray[idx] = self.array[idx]

        #update the new array
        self.array = newArray
        #after array is created successfully, change the capacity
        self.capacity = newCapacity


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
