# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float("inf")
        for price in prices:
            if min_price < price:
                profit = max(price - min_price, profit)
            else:
                min_price = price
        return profit


testcases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]

for testcase in testcases:
    print(Solution().maxProfit(testcase))
