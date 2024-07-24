# [155. Min Stack](https://leetcode.com/problems/min-stack/)


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.min_stack) or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = None
        if self.stack:
            val = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == val:
            self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
