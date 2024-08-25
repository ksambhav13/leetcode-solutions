# [803. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        cheapest = [-1] * n
        cheapest[src] = 0

        for i in range(k + 1):
            tmp = cheapest.copy()
            for s, d, p in flights:
                if cheapest[s] == -1:
                    continue
                if tmp[d] == -1:
                    tmp[d] = cheapest[s] + p
                elif cheapest[s] + p < tmp[d]:
                    tmp[d] = cheapest[s] + p
            cheapest = tmp
            print(f"{i=} {cheapest=}")
        return cheapest[dst]


testcases = [
    # 4,
    # [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
    # 0,
    # 3,
    # 2,
    # 3,
    # [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
    # 0,
    # 2,
    # 1,
    # 3,
    # [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
    # 0,
    # 2,
    # 0,
    # 4,
    # [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
    # 0,
    # 3,
    # 1,
    5,
    [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]],
    0,
    2,
    2,
]


for i in range(0, len(testcases), 5):
    print(
        Solution().findCheapestPrice(
            testcases[i],
            testcases[i + 1],
            testcases[i + 2],
            testcases[i + 3],
            testcases[i + 4],
        )
    )
