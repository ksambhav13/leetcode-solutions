# [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if target in memo:
                return memo[target]
            res = 0
            for num in nums:
                res += dfs(target - num)
            memo[target] = res
            return res

        return dfs(target)

    def combinationSum4WithoutMemo(self, nums: List[int], target: int) -> int:
        self.count = 0

        def dfs(target):
            if target < 0:
                return
            if target == 0:
                self.count += 1
                return
            for num in nums:
                dfs(target - num)

        dfs(target)
        return self.count


testcases = [
    [1, 2, 3],
    4,
    [9],
    3,
    [4, 2, 1],
    32,
]


for i in range(0, len(testcases), 2):
    print(Solution().combinationSum4(testcases[i], testcases[i + 1]))
