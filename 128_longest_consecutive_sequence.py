# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        res = 0
        for num in nums:
            if num - 1 in uniques:
                continue
            t = 1
            while num + t in uniques:
                t += 1
            if t > res:
                res = t
        return res


testcases = [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
]


for testcase in testcases:
    print(Solution().longestConsecutive(testcase))
