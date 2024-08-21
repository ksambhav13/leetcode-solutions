# [221. Maximal Square](https://leetcode.com/problems/maximal-square/)


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        longest = 0
        memo = {}

        def get_max(i, j):
            if i >= m or j >= n:
                return 0
            if matrix[i][j] == "0":
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            res = 1 + min(get_max(i + 1, j), get_max(i, j + 1), get_max(i + 1, j + 1))
            memo[(i, j)] = res
            return res

        for i in range(m):
            for j in range(n):
                k = get_max(i, j)
                longest = max(k, longest)
        return longest * longest


testcases = [
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ],
    [["0", "1"], ["1", "0"]],
    [["0"]],
]


for testcase in testcases:
    print(Solution().maximalSquare(testcase))
