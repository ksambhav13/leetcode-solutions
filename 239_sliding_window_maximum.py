# [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)


from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = deque()
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            if i - k >= stack[0]:
                stack.popleft()

            if i >= k - 1:
                res.append(nums[stack[0]])
        return res


# [1, 3, -1, -3, 5, 3, 6, 7]
testcases = [
    [1, 3, -1, -3, 0, 5, 3, 6, 7],
    3,
    [1],
    1,
]


for i in range(0, len(testcases), 2):
    print(Solution().maxSlidingWindow(testcases[i], testcases[i + 1]))
