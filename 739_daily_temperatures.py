# [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)


from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                k = stack.pop()
                res[k] = i - k
            stack.append(i)

        return res

    def dailyTemperaturesCache(self, temperatures: List[int]) -> List[int]:
        memo = {}
        for i in range(len(temperatures) - 1, -1, -1):
            min_days = len(temperatures)
            for t, j in memo.items():
                if t > temperatures[i] and (j - i) < min_days:
                    min_days = j - i
            memo[temperatures[i]] = i
            temperatures[i] = min_days if min_days < len(temperatures) else 0
        return temperatures

    def dailyTemperaturesBrute(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(0, len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
            else:
                res.append(0)

        return res


testcases = [
    [73, 74, 75, 71, 69, 72, 76, 73],
    [30, 40, 50, 60],
    [30, 60, 90],
]


for testcase in testcases:
    print(Solution().dailyTemperatures(testcase))
