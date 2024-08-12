# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


testcases = [
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [3, 3, 3, 3, 3],
]


for testcase in testcases:
    print(Solution().findDuplicate(testcase))
