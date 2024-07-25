# [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

from typing import List, Set


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = {}

        def dp(t: int) -> List[List[int]]:
            if t < 0:
                return []
            if t == 0:
                return [[]]
            if t in cache:
                return cache[t]
            res = []
            for c in candidates:
                resi = dp(t - c)
                for ri in resi:
                    temp = sorted([c] + ri)
                    if temp not in res:
                        res.append(temp)
            cache[t] = res
            return res

        return dp(target)


testcases = [
    [2, 3],
    5,
    [2, 3, 6, 7],
    7,
    [2, 3, 5],
    8,
    [2],
    1,
]

for i in range(0, len(testcases), 2):
    print(Solution().combinationSum(testcases[i], testcases[i + 1]))
