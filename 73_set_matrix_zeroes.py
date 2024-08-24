# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = 1
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        zero_row = 0
                    else:
                        matrix[i][0] = 0
        print(f"{zero_row=}")
        print("iter 1 ", matrix)
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        for j, cell in enumerate(matrix[0]):
            if cell == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        print("iter 2 ", matrix)

        if zero_row == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        return matrix


testcases = [
    # [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    # [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
    [
        [-4, -2147483648, 6, -7, 0],
        [-8, 6, -8, -6, 0],
        [2147483647, 2, -9, -6, -10],
    ],
]


for testcase in testcases:
    print(Solution().setZeroes(testcase))
