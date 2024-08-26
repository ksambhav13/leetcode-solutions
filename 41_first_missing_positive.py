# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0

        for i, num in enumerate(nums):
            idx = abs(num) - 1
            if idx >= 0 and idx < len(nums):
                if nums[idx] == 0:
                    nums[idx] = -(len(nums) + 1)
                elif nums[idx] > 0:
                    nums[idx] = -nums[idx]
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1


testcases = [
    [1, 2, 0],
    [3, 2, 1, 0],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12],
    [0, 1, 4, -9],
]


for testcase in testcases:
    print(Solution().firstMissingPositive(testcase))
