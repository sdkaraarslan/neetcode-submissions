class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # were gonna push the min values here

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            x = min(val, self.minStack[-1])
            self.minStack.append(x)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
