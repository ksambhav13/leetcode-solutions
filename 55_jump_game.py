# [55. Jump Game](https://leetcode.com/problems/jump-game/)


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumped = 0
        for i, num in enumerate(nums):
            jumped = max(jumped, i + num)
            if jumped >= len(nums) - 1:
                return True
            if num == 0 and jumped <= i:
                return False


testcases = [
    [2, 3, 1, 1, 4],
    [3, 2, 1, 0, 4],
    [2, 0, 0],
]


for testcase in testcases:
    print(Solution().canJump(testcase))
