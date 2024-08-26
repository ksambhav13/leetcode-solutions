# [1019. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        r = 0
        while r < len(nums) and nums[r] < 0:
            r += 1
        l = r - 1
        while l >= 0 or r < len(nums):
            if l < 0:
                res.append(nums[r] ** 2)
                r += 1
            elif r >= len(nums):
                res.append(nums[l] ** 2)
                l -= 1
            elif nums[r] > -nums[l]:
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
        return res


testcases = [
    [-4, -1, 0, 3, 10],
    [-7, -3, 2, 3, 11],
    [-2, -1],
    [1, 2],
    [-1, 2],
    [-2, 1],
]


for testcase in testcases:
    print(Solution().sortedSquares(testcase))
