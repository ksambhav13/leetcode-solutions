# [78. Subsets](https://leetcode.com/problems/subsets/)


from collections import deque
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            count = len(result)
            for p in result[0:count]:
                result.append(p + [num])

        return result


testcases = [
    [1, 2, 3],
    [0],
]


for testcase in testcases:
    print(Solution().subsets(testcase))
