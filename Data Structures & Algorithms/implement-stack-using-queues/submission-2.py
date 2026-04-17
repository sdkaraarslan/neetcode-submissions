"""
Implement Stack Using Queues:

queue: FIFO >> first in first out, pop from left, push from left >> deque()
stack: LIFO >> last in first out, pop from right, push from left
e needs to be popped
[a,b,c,d,e] pop a from left, push a to end
[c,d,e,a,b] pop a from left, push a to end
[d,e,a,b,c] pop a from left, push a to end
[e,a,b,c,d] pop a from left, push a to end
[a,b,c,d] e is popped from left and returned

S.C.
T.C.
"""

class MyStack:

    def __init__(self):
        self.queuedStack = deque()

    def push(self, x: int) -> None:
        self.queuedStack.append(x)

    def pop(self) -> int:
        for i in range(len(self.queuedStack)-1):
            self.queuedStack.append(self.queuedStack.popleft())
        return self.queuedStack.popleft()

    def top(self) -> int:
        return self.queuedStack[-1]

    def empty(self) -> bool:
        return len(self.queuedStack)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()