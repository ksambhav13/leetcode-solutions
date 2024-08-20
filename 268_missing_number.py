# [268. Missing Number](https://leetcode.com/problems/missing-number/)


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        for num in nums:
            total -= num
        return total


testcases = [
    [3, 0, 1],
    [0, 1],
    [9, 6, 4, 2, 3, 5, 7, 0, 1],
]


for testcase in testcases:
    print(Solution().missingNumber(testcase))
