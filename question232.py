# [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

from collections import deque


class MyQueue2:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


class MyQueue:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def _move(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        if not self.stack2:
            self._move()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            self._move()
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.stack1, obj.stack2)
param_2 = obj.pop()
print(obj.stack1, obj.stack2)
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)
