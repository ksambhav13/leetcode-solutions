# [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        waterp = [[0] * n for _ in range(m)]

        dirs = [0, 1, 0, -1, 0]
        res = []

        def dfsp(r, c):
            if waterp[r][c] == cur:
                return
            if waterp[r][c] == req:
                res.append([r, c])

            waterp[r][c] = cur
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i + 1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if heights[nr][nc] >= heights[r][c]:
                        dfsp(nr, nc)

        cur, req = 1, -1
        for i in range(n):
            dfsp(0, i)
        for j in range(m):
            dfsp(j, 0)

        cur, req = 2, 1
        for i in range(n):
            dfsp(m - 1, i)
        for j in range(m):
            dfsp(j, n - 1)

        return res


testcases = [
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ],
    [[1]],
]


for testcase in testcases:
    print(Solution().pacificAtlantic(testcase))
