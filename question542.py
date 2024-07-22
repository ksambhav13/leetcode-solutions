# [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = [0, 1, 0, -1, 0]
        m = len(mat)
        n = len(mat[0]) if mat else 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            (r, c) = q.popleft()
            val = mat[r][c] + 1
            for i in range(4):
                nr, nc = r + direction[i], c + direction[i + 1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = val
                q.append((nr, nc))
        return mat


testcases = [
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
]

for testcase in testcases:
    print(Solution().updateMatrix(testcase))
