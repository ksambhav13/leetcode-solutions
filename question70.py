# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)


class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dp(s: int):
            if s < 0:
                return 0
            if s == 0:
                return 1
            if s in mem:
                return mem.get(s)
            steps = dp(s - 1) + dp(s - 2)
            mem[s] = steps
            return steps

        return dp(n)


testcases = [2, 3]

for testcase in testcases:
    print(Solution().climbStairs(testcase))
