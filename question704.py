# [704. Binary Search](https://leetcode.com/problems/binary-search/)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            mid: int = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

    def search_recursive(self, nums: List[int], target: int) -> int:
        def binary_search(i: int, j: int):
            if i > j:
                return -1
            mid: int = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, j)
            else:
                return binary_search(i, mid - 1)

        return binary_search(0, len(nums) - 1)


testcases = [
    [-1, 0, 3, 5, 9, 12],
    9,
    [-1, 0, 3, 5, 9, 12],
    2,
    [],
    5,
    [4],
    4,
]

for i in range(0, len(testcases), 2):
    print(Solution().search(testcases[i], testcases[i + 1]))
