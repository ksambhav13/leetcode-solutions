# [189. Rotate Array](https://leetcode.com/problems/rotate-array/)


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k >= len(nums):
            k = k - len(nums)
        print(f"{k=}")
        last = [0] * k
        for i in range(k):
            p = i
            num = nums[i]
            while p + k < len(nums):
                p = p + k
                temp = nums[p]
                nums[p] = num
                num = temp
            last[p + k - len(nums)] = num
        for i in range(k):
            nums[i] = last[i]
        return nums


testcases = [
    [1, 2, 3, 4, 5, 6, 7],
    3,
    [-1, -100, 3, 99],
    2,
    [-1],
    2,
    [1, 2],
    5,
]


for i in range(0, len(testcases), 2):
    print(Solution().rotate(testcases[i], testcases[i + 1]))
