# [1. Two Sum](https://leetcode.com/problems/two-sum/)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in temp:
                return [temp[diff], i]
            temp[num] = i


testcases = [
    [2, 7, 11, 15],
    9,
    [3, 2, 4],
    6,
    [3, 3],
    6,
]

for i in range(0, len(testcases), 2):
    print(Solution().twoSum(testcases[i], testcases[i + 1]))
