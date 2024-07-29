# [79. Word Search](https://leetcode.com/problems/word-search/)


from collections import deque
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [0, 1, 0, -1, 0]
        m = len(board)
        n = len(board[0])
        path = set()

        def dfs(i, j, l):
            if l == len(word):
                return True
            if (i * n + j) in path:
                return False

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[l]:
                return False

            path.add(n * i + j)
            res = False
            for k in range(4):
                res = res or dfs(i + dirs[k], j + dirs[k + 1], l + 1)

            path.remove(n * i + j)
            return res

        for i, bi in enumerate(board):
            for j, v in enumerate(bi):
                if v == word[0]:
                    res = dfs(i, j, 0)
                    if res:
                        return res

        return False


testcases = [
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    "ABCCED",
    [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ],
    "SEE",
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    "ABCB",
    [["a", "a"]],
    "aaa",
    [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"],
    ],
    "ABCESEEEFS",
]


for i in range(0, len(testcases), 2):
    print(Solution().exist(testcases[i], testcases[i + 1]))
