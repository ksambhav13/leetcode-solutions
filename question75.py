# [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def countsort():
            counts = [0, 0, 0]
            for num in nums:
                counts[num] += 1
            k = 0
            for i, c in enumerate(counts):
                for j in range(c):
                    nums[k] = i
                    k += 1

        def quicksort(i, j):
            if i >= j:
                return
            l, r = i - 1, i
            while r < j:
                if nums[r] <= nums[j]:
                    l += 1
                    nums[l], nums[r] = nums[r], nums[l]
                r += 1

            nums[l + 1], nums[j] = nums[j], nums[l + 1]

            quicksort(i, l)
            quicksort(l + 2, j)

        # quicksort(0, len(nums) - 1)
        countsort()


testcases = [
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
]

for testcase in testcases:
    Solution().sortColors(testcase)
    print(testcase)
