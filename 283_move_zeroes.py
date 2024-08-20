# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zindex = 0
        while zindex < len(nums):
            if nums[zindex] == 0:
                break
            zindex += 1
        for i in range(zindex + 1, len(nums)):
            if nums[i] != 0:
                nums[zindex] = nums[i]
                nums[i] = 0
                zindex += 1

        return nums


testcases = [
    [0, 1, 0, 3, 12, 0, 0, 0, 5, 0, 9, 1, 0],
    [0],
    [2, 1, 0, 1, 0, 0, 8],
]


for testcase in testcases:
    print(Solution().moveZeroes(testcase))
