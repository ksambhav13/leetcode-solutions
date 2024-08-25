# [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        sign = "+"
        for ch in s + "+":
            if ch == " ":
                continue
            if ch.isdigit():
                cur = (cur * 10) + int(ch)
            else:
                if sign == "+":
                    stack.append(cur)
                elif sign == "-":
                    stack.append(-cur)
                elif sign == "*":
                    stack.append(stack.pop() * cur)
                elif sign == "/":
                    stack.append(int(stack.pop() / cur))
                cur = 0
                sign = ch
        return sum(stack)


testcases = [
    # "33+2*2",
    # " 3/2 ",
    # " 3+5 / 2 ",
    # "2+2*3*2",
    # "1-1+1",
    # "1 + 1 - 1",
    # "1-1-1",
    "1+2*5/3+6/4*2",
]

2 - 2 + 2


for testcase in testcases:
    print(Solution().calculate(testcase))
