# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0
        for num in nums:
            sum += num
            if sum > maxSum:
                maxSum = sum
            if sum < 0:
                sum = 0

        return maxSum


testcases = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5, 4, -1, 7, 8],
    [-1, -2],
]

for testcase in testcases:
    print(Solution().maxSubArray(testcase))
