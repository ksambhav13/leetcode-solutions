# [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[0] < nums[-1]:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[mid] < nums[0]:
                r = mid
        return nums[r]


testcases = [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [11, 13, 15, 17],
    [3, 1, 2],
    [2, 1],
    [1, 2],
]


for testcase in testcases:
    print(Solution().findMin(testcase))
