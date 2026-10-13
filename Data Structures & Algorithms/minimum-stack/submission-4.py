import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        self.minV = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minV > val:
            self.minV = val
        self.prefix.append(self.minV)

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

        self.minV = self.prefix[-1] if self.prefix else math.inf

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minV