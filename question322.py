# [322. Coin Change](https://leetcode.com/problems/coin-change/)

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_cache = {}
        max = amount + 1

        def min_required(ca):
            if ca < 0:
                return max
            if ca == 0:
                return 0
            if ca in coins:
                return 1
            if ca in min_cache:
                return min_cache[ca]

            cmin = min([min_required(ca - coin) for coin in coins])
            min_cache[ca] = 1 + cmin
            return 1 + cmin

        res = min_required(amount)
        return -1 if res >= max else res


testcases = [
    [1, 2, 5],
    110,
    [2],
    3,
    [1],
    0,
    [2, 4],
    67,
]

for i in range(0, len(testcases), 2):
    print(Solution().coinChange(testcases[i], testcases[i + 1]))
