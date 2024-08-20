# [136. Single Number](https://leetcode.com/problems/single-number/)


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return next(iter(s))


testcases = [
    [2, 2, 1],
    [4, 1, 2, 1, 2],
    [1],
    [-1, -1, -2],
    [4, 2, 4],
]


for testcase in testcases:
    print(Solution().singleNumber(testcase))
