# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, mx, mn = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                mx, mn = 1, 1
                res = max(res, 0)
                continue
            mx, mn = (
                max(mx * nums[i], mn * nums[i], nums[i]),
                min(mx * nums[i], mn * nums[i], nums[i]),
            )
            if mx > res:
                res = mx

        return res


testcases = [
    [2, 3, -2, 4],
    [-2, 0, -1],
    [-2, 4, 2],
    [0, 2],
    [2, -5, -2, -4, 3],
]


for testcase in testcases:
    print(Solution().maxProduct(testcase))
