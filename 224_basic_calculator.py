# [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)


from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        sign, output, cur = 1, 0, 0
        for op in s:
            if op.isdigit():
                cur = (cur * 10) + int(op)
            else:
                output += sign * cur
                cur = 0

            if op == "+":
                sign = 1
            elif op == "-":
                sign = -1
            elif op == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif op == ")":
                output = stack.pop() * output + stack.pop()

        return output + (cur * sign)


testcases = [
    "1 + 13",
    " 2-1 + 2 ",
    "(1+(4+5+2)-3)+(6+8)",
]


for testcase in testcases:
    print(Solution().calculate(testcase))

#     +

# 1       *

#     3       5
