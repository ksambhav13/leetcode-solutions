# [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            append = True
            while stack and num < 0 < stack[-1]:
                if stack[-1] < -num:
                    stack.pop()
                    continue
                elif stack[-1] == -num:
                    stack.pop()
                append = False
                break
            if append:
                stack.append(num)
        return stack


testcases = [
    [5, 10, -5],
    [8, -8],
    [10, 2, -5],
    [-2, -1, 1, 2],
    [-2, -2, 1, -2],
    [5, -8, -10],
]


for testcase in testcases:
    print(Solution().asteroidCollision(testcase))
