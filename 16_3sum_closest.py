# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = float("inf")
        res = -1
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return target
                if abs(target - s) < max_diff:
                    res = s
                    max_diff = abs(target - s)
        return res


testcases = [
    [-1, 2, 1, -4],
    1,
    [0, 0, 0],
    1,
    [1, 1, 1, 0],
    -100,
]


for i in range(0, len(testcases), 2):
    print(Solution().threeSumClosest(testcases[i], testcases[i + 1]))
