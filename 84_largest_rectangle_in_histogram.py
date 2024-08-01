# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)


from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = deque()
        for i, height in enumerate(heights):
            k = i
            while stack and stack[-1][0] > height:
                (h, k) = stack.pop()
                max_area = max(max_area, h * (i - k))
            stack.append((height, k))
        while stack:
            (h, k) = stack.pop()
            max_area = max(max_area, h * (len(heights) - k))
        return max_area

    def largestRectangleAreaBruteForce(self, heights: List[int]) -> int:
        max_area = heights[0]
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i + 1, len(heights)):
                if heights[j] < min_height:
                    min_height = heights[j]
                area = min_height * (j - i + 1)
                if area > max_area:
                    max_area = area

        return max_area


testcases = [
    [2, 1, 5, 6, 2, 3],
    [2, 4],
    [2, 1, 2],
]


for testcase in testcases:
    print(Solution().largestRectangleArea(testcase))
