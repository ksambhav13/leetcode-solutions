# [15. 3Sum](https://leetcode.com/problems/3sum/)

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while left < right:
                currentSum = nums[left] + nums[right]

                if currentSum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
        return res


testcases = [
    [-1, 0, 1, 2, -1, -4],
    [0, 1, 1],
    [0, 0, 0],
]

for testcase in testcases:
    print(Solution().threeSum(testcase))
