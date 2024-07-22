# [169. Majority Element](https://leetcode.com/problems/majority-element/)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate


testcases = [
    [3, 2, 3],
    [2, 2, 1, 1, 1, 2, 2],
]

for testcase in testcases:
    print(Solution().majorityElement(testcase))
