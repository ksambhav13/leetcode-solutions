# [134. Gas Station](https://leetcode.com/problems/gas-station/)


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        if sum_cost > sum_gas:
            return -1
        current_gas = 0
        res = 0
        for i, g in enumerate(gas):
            current_gas += g - cost[i]
            if current_gas < 0:
                res = i + 1
        return res


testcases = [
    [1, 2, 3, 4, 5],
    [3, 4, 5, 1, 2],
    [2, 3, 4],
    [3, 4, 3],
]


for i in range(0, len(testcases), 2):
    print(Solution().canCompleteCircuit(testcases[i], testcases[i + 1]))
