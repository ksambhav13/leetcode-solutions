# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        n = len(nums)
        for i in range(1, n):
            res.append(res[i - 1] * nums[i - 1])
        t = 1
        for i in range(n - 2, -1, -1):
            t *= nums[i + 1]
            res[i] = res[i] * t

        return res


testcases = [
    [5, 2, 3, 4],
    [-1, 1, 0, -3, 3],
]

for testcase in testcases:
    print(Solution().productExceptSelf(testcase))
