# [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                return True
        row = l - 1
        if row < 0:
            return False
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False


testcases = [
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
    3,
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
    13,
    [[1]],
    1,
]


for i in range(0, len(testcases), 2):
    print(Solution().searchMatrix(testcases[i], testcases[i + 1]))
