# [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)


import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l : l + k]

    def findClosestElementsBinary(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                idx = mid
                break
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        if idx < 0:
            if l - 1 < 0:
                idx = 0
            elif l >= len(arr):
                idx = l - 1
            elif x - arr[l - 1] <= arr[l] - x:
                idx = l - 1
            else:
                idx = l
        i, j = idx, idx
        for _ in range(k - 1):
            if i - 1 >= 0 and j + 1 < len(arr) - 1:
                if x - arr[i - 1] <= arr[j + 1] - x:
                    i -= 1
                else:
                    j += 1
            elif i - 1 >= 0:
                i -= 1
            elif j + 1 < len(arr):
                j += 1
        return arr[i : j + 1]


testcases = [
    # [1, 2, 3, 8, 9],
    # 1,
    # 4,
    # [1, 2, 3, 4, 5],
    # 4,
    # -1,
    [3, 5, 8, 10],
    2,
    15,
]


for i in range(0, len(testcases), 3):
    print(
        Solution().findClosestElements(testcases[i], testcases[i + 1], testcases[i + 2])
    )
