# [179. Largest Number](https://leetcode.com/problems/largest-number/)


from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=cmp_to_key(lambda s1, s2: int(s2 + s1) - int(s1 + s2)))
        return "".join(nums)


testcases = [
    [10, 2, 0],
    [30, 3, 34, 5, 9],
    [313, 31],
    [432, 43243],
    [0, 0],
]

31331
31313


for testcase in testcases:
    print(Solution().largestNumber(testcase))
