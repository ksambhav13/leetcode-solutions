# [51. N-Queens](https://leetcode.com/problems/n-queens/)


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()

        res = []

        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                resi = ["".join(row) for row in board]
                res.append(resi)
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                board[r][c] = "Q"
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res


testcases = [
    4,
    1,
    9,
]


for testcase in testcases:
    print(Solution().solveNQueens(testcase))
