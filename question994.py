# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [0, 1, 0, -1, 0]
        rotten = deque()
        fresh = 0
        m = len(grid)
        n = len(grid[0]) if grid else 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        max_days = 0
        while rotten:
            (r, c, count) = rotten.popleft()
            max_days = max(max_days, count)
            for k in range(4):
                nr, nc = r + direction[k], c + direction[k + 1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                rotten.append((nr, nc, count + 1))
                fresh -= 1
        if fresh > 0:
            return -1
        else:
            return max_days


testcases = [
    [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
    [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
    [[0, 2]],
]

for testcase in testcases:
    print(Solution().orangesRotting(testcase))
