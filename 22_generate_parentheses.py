# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def addP(start, open, close):
            if (open + close) == 2 * n:
                res.append(start)
                return
            if open < n:
                addP(start + "(", open + 1, close)
            if open > close:
                addP(start + ")", open, close + 1)

        addP("", 0, 0)
        return res


testcases = [
    3,
    # 1,
]


for testcase in testcases:
    print(Solution().generateParenthesis(testcase))
