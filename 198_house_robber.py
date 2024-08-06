# [198. House Robber](https://leetcode.com/problems/house-robber/)


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            if i in memo:
                return memo[i]
            #  if i is robbed
            ri = nums[i] + dfs(i + 2)
            # if i is not robbed
            re = dfs(i + 1)
            res = max(ri, re)
            memo[i] = res
            return res

        return dfs(0)


testcases = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1],
]


for testcase in testcases:
    print(Solution().rob(testcase))
