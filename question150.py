# [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(a: int, b: int, op: str):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return int(a / b)

        stack = deque()
        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()
                val = operate(a, b, t)
                stack.append(val)
            else:
                stack.append(int(t))

        return stack.pop()


testcases = [
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
]

for testcase in testcases:
    print(Solution().evalRPN(testcase))
