# [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                sqidx = (r // 3) * 3 + (c // 3)
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sq[sqidx].add(board[r][c])

        def backtrack(r, c):
            if c >= 9:
                c = 0
                r += 1

            if r == 9:
                return True

            if board[r][c] != ".":
                return backtrack(r, c + 1)

            sqidx = (r // 3) * 3 + (c // 3)
            for i in range(1, 10):
                ch = str(i)
                if ch in row[r] or ch in col[c] or ch in sq[sqidx]:
                    continue
                board[r][c] = ch
                row[r].add(ch)
                col[c].add(ch)
                sq[sqidx].add(ch)

                success = backtrack(r, c + 1)
                if success:
                    return True
                else:
                    board[r][c] = "."
                    row[r].remove(ch)
                    col[c].remove(ch)
                    sq[sqidx].remove(ch)

            return False

        success = backtrack(0, 0)
        if success:
            return board
        else:
            return None


testcases = [
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
]


for testcase in testcases:
    print(Solution().solveSudoku(testcase))
