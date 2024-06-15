class MinStack:
    def __init__(self):
        self.minValue = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.minValue and self.minValue[-1] < val:
            self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(val)
        self.stack.append(val) 

    def pop(self) -> None:
        if not self.stack:
            return []
        self.minValue.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValue[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()