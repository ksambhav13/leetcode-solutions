# [48. Rotate Image](https://leetcode.com/problems/rotate-image/)


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for r in matrix:
            r.reverse()
        return matrix

    def rotateFirst(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dirs = [0, 1, 0, -1, 0]

        def rot(initial, nr):
            dir = 0
            (pi, pj) = initial
            cur = matrix[pi][pj]
            for i in range(4 * nr - 4):
                dir = i // (nr - 1)
                pi, pj = pi + dirs[dir], pj + dirs[dir + 1]
                tmp = matrix[pi][pj]
                matrix[pi][pj] = cur
                cur = tmp

        n = len(matrix)

        for i in range(n // 2):
            for _ in range((n - 2 * i) - 1):
                rot((i, i), n - (2 * i))

        return matrix


testcases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    [[1]],
    [[1, 2], [3, 4]],
]

[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
]

for testcase in testcases:
    print(Solution().rotate(testcase))
