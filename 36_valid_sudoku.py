# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)


from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == ".":
                    continue
                if (
                    digit in rows[i]
                    or digit in cols[j]
                    or digit in square[(i // 3) * 3 + (j // 3)]
                ):
                    return False
                rows[i].add(digit)
                cols[j].add(digit)
                square[(i // 3) * 3 + (j // 3)].add(digit)
        return True

    def isValidSudokuPrimitive(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check = [True] * 9
            for j in range(9):
                if not board[i][j].isdigit():
                    continue
                num = int(board[i][j])
                if not check[num - 1]:
                    return False
                else:
                    check[num - 1] = False
        for i in range(9):
            check = [True] * 9
            for j in range(9):
                if not board[j][i].isdigit():
                    continue
                num = int(board[j][i])
                if not check[num - 1]:
                    return False
                else:
                    check[num - 1] = False
        for i in range(9):
            si, sj = (i // 3) * 3, (i % 3) * 3
            check = [True] * 9
            for j in range(9):
                k, l = si + (j // 3), sj + (j % 3)
                if not board[k][l].isdigit():
                    continue
                num = int(board[k][l])
                if not check[num - 1]:
                    return False
                else:
                    check[num - 1] = False
        return True


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
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
    print(Solution().isValidSudoku(testcase))
