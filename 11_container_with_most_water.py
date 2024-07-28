# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_h = min(height[l], height[r]) * (r - l)

        while l < r:
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
            max_h = max(max_h, min(height[l], height[r]) * (r - l))
        return max_h


testcases = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 1],
]


for testcase in testcases:
    print(Solution().maxArea(testcase))
