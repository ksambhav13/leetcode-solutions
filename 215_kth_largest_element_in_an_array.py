# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)


import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []
        for i in range(k):
            heapq.heappush(data, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > data[0]:
                heapq.heapreplace(data, nums[i])
        return data[0]


testcases = [
    [3, 2, 1, 5, 6, 4],
    2,
    [3, 2, 3, 1, 2, 4, 5, 5, 6],
    4,
]


for i in range(0, len(testcases), 2):
    print(Solution().findKthLargest(testcases[i], testcases[i + 1]))
