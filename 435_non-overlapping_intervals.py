# [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        removal = 0
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
                continue
            removal += 1
            if prev_end > end:
                prev_end = end
        return removal


testcases = [
    [[1, 2], [2, 3], [3, 4], [1, 3]],
    [[1, 2], [1, 2], [1, 2]],
    [[1, 2], [2, 3]],
]


for testcase in testcases:
    print(Solution().eraseOverlapIntervals(testcase))
