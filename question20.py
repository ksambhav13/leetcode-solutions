# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        closing_braces_dict = {")": "(", "}": "{", "]": "["}
        stack = deque()
        for c in s:
            if c in closing_braces_dict:
                if not stack:
                    return False
                if stack.pop() != closing_braces_dict[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


testcases = ["()", "()[]{}", "(]"]

for testcase in testcases:
    print(Solution().isValid(testcase))
