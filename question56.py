# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        s_intervals = sorted(intervals)
        cur = s_intervals[0]

        for interval in s_intervals:
            if interval[0] <= cur[1]:
                cur = [cur[0], max(cur[1], interval[1])]
            else:
                res.append(cur)
                cur = interval
        res.append(cur)
        return res


testcases = [
    [[1, 3], [8, 10], [15, 18], [2, 6]],
    [[1, 4], [4, 5]],
]

for testcase in testcases:
    print(Solution().merge(testcase))
