# [57. Insert Interval](https://leetcode.com/problems/insert-interval/)

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        merged = newInterval
        for t in intervals:
            if merged:
                if t[1] < merged[0]:
                    res.append(t)
                elif t[0] > merged[1]:
                    res.append(merged)
                    merged = None
                    res.append(t)
                else:
                    merged = [min(t[0], merged[0]), max(t[1], merged[1])]
            else:
                res.append(t)
        if merged:
            res.append(merged)
        return res


testcases = [
    [[1, 3], [6, 9]],
    [2, 5],
    [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
    [4, 8],
]

for i in range(0, len(testcases), 2):
    print(Solution().insert(testcases[i], testcases[i + 1]))
