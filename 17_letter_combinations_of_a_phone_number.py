# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)


from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        q = deque()
        q.append("")
        for digit in digits:
            ltrs = letters[int(digit) - 2]
            print(f"{ltrs=}")
            l = len(q)
            for _ in range(l):
                start = q.popleft()
                for ch in ltrs:
                    news = start + ch
                    print(f"{news=}")
                    if len(news) == len(digits):
                        res.append(news)
                    else:
                        q.append(news)
        return res


testcases = [
    "23",
    "",
    "2",
]


for testcase in testcases:
    print(Solution().letterCombinations(testcase))
