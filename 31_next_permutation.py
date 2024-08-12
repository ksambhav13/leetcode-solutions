# [31. Next Permutation](https://leetcode.com/problems/next-permutation/)


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        print(f"{i=}")
        if i < 0:
            nums.reverse()
            return nums

        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


testcases = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
]


for testcase in testcases:
    print(Solution().nextPermutation(testcase))
