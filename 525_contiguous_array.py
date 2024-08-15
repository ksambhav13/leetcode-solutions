# [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        diff_index = {}
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                diff += 1
            else:
                diff -= 1

            if diff == 0:
                res = i + 1
            elif diff in diff_index:
                res = max(res, i - diff_index[diff])
            else:
                diff_index[diff] = i
        return res


testcases = [
    [0, 1],
    [0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0],
]


for testcase in testcases:
    print(Solution().findMaxLength(testcase))
