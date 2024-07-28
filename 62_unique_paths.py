# [62. Unique Paths](https://leetcode.com/problems/unique-paths/)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        cache[m * n - 1] = 1

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            idx = n * i + j
            if idx in cache:
                return cache[idx]

            cache[idx] = dfs(i + 1, j) + dfs(i, j + 1)

            return cache[idx]

        return dfs(0, 0)


testcases = [
    3,
    7,
    3,
    2,
    100,
    100,
]


for i in range(0, len(testcases), 2):
    print(Solution().uniquePaths(testcases[i], testcases[i + 1]))
