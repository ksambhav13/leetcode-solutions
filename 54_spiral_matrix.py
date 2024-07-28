# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m = len(matrix)
        n = len(matrix[0])
        dirs = [0, 1, 0, -1, 0]

        cur_dir = 0
        cur_r = 0
        cur_c = -1
        brake = False
        while True:
            next_r = cur_r + dirs[cur_dir]
            next_c = cur_c + dirs[cur_dir + 1]

            if (
                next_r >= m
                or next_r < 0
                or next_c >= n
                or next_c < 0
                or matrix[next_r][next_c] is None
            ):
                if brake:
                    break
                cur_dir += 1
                cur_dir = cur_dir if cur_dir < 4 else cur_dir - 4
                brake = True
            else:
                cur_r, cur_c = next_r, next_c
                output.append(matrix[cur_r][cur_c])
                matrix[cur_r][cur_c] = None
                brake = False
        return output


testcases = [
    [[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
]


for testcase in testcases:
    print(Solution().spiralOrder(testcase))
