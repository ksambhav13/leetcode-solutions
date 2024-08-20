# [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)


class Solution:
    i = 0

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1.0
        if n == -1:
            return 1 / x
        self.i += 1

        res = self.myPow(x, n // 2)
        print(f"iter {self.i} {res=}")
        res *= res
        return res * x if n % 2 else res


testcases = [
    # 2.00000,
    # 1000,
    2.10000,
    3,
    # 2.00000,
    # -3,
    # 0.00001,
    # 2147483647,
]


for i in range(0, len(testcases), 2):
    print(Solution().myPow(testcases[i], testcases[i + 1]))
