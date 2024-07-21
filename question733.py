# [733. Flood Fill](https://leetcode.com/problems/flood-fill/)

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        target = image[sr][sc]
        if target == color:
            return image

        def flood_fill_internal(i, j):
            if i >= len(image) or i < 0:
                return
            if j >= len(image[i]) or j < 0:
                return
            if image[i][j] == target:
                image[i][j] = color
                flood_fill_internal(i, j + 1)
                flood_fill_internal(i, j - 1)
                flood_fill_internal(i + 1, j)
                flood_fill_internal(i - 1, j)

        flood_fill_internal(sr, sc)
        return image


testcases = [
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
    1,
    1,
    2,
    [[0, 0, 0], [0, 0, 0]],
    0,
    0,
    0,
]

for i in range(0, len(testcases), 4):
    image, sr, sc, color = (
        testcases[i],
        testcases[i + 1],
        testcases[i + 2],
        testcases[i + 3],
    )
    print(Solution().floodFill(image, sr, sc, color))
