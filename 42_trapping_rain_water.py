# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        w = 0
        while l < r:
            if maxl <= maxr:
                l += 1
                if height[l] < maxl:
                    w += maxl - height[l]
                else:
                    maxl = height[l]
            else:
                r -= 1
                if height[r] < maxr:
                    w += maxr - height[r]
                else:
                    maxr = height[r]
        return w

    def trapWithMemory(self, height: List[int]) -> int:
        n = len(height)
        largest_left = [0] * n
        largest_right = [0] * n

        lhigh = 0
        for i in range(0, n):
            largest_left[i] = lhigh
            if height[i] > lhigh:
                lhigh = height[i]
        rhigh = 0
        for i in range(n - 1, -1, -1):
            largest_right[i] = rhigh
            if height[i] > rhigh:
                rhigh = height[i]
        water_stored = 0
        for i, h in enumerate(height):
            mh = min(largest_left[i], largest_right[i])
            if mh > h:
                water_stored += mh - h

        return water_stored


testcases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
]


for testcase in testcases:
    print(Solution().trap(testcase))
