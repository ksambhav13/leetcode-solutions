# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False


testcases = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
]

for testcase in testcases:
    print(Solution().containsDuplicate(testcase))
