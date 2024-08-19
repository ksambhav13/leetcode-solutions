# [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)


from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        m, n = len(matrix), len(matrix[0])
        dirs = [0, 1, 0, -1, 0]

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            res = 1
            for k in range(4):
                ni, nj = i + dirs[k], j + dirs[k + 1]
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            memo[(i, j)] = res
            return res

        max_res = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j) > max_res:
                    max_res = dfs(i, j)
        return max_res


testcases = [
    [[9, 9, 4], [6, 6, 8], [2, 1, 1]],
    [[3, 4, 5], [3, 2, 6], [2, 2, 1]],
    [[1]],
]


for testcase in testcases:
    print(Solution().longestIncreasingPath(testcase))
