# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)


from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "-1"
            for k in range(4):
                ni, nj = i + direction[k], j + direction[k + 1]
                dfs(ni, nj)

        direction = [0, 1, 0, -1, 0]
        count = 0
        m = len(grid)
        n = len(grid[0]) if grid else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count


testcases = [
    # [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"],
    # ],
    # [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"],
    # ],
    # [["1", "0", "1", "1", "0", "1", "1"]],
]

for testcase in testcases:
    print(Solution().numIslands(testcase))
