# [912. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)
from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_total = [0] * len(w)
        self.prefix_total[0] = self.w[0]
        for i in range(1, len(self.prefix_total)):
            self.prefix_total[i] = self.prefix_total[i - 1] + self.w[i]
        self.total = self.prefix_total[-1]
        print("prefix total: ", self.prefix_total)
        random.seed(0)

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        left, right = 0, len(self.prefix_total) - 1
        print(f"{rand=}")
        res = right
        while left <= right:
            mid = (left + right) // 2
            if self.prefix_total[mid] > rand:
                res = mid
                right = mid - 1
            elif self.prefix_total[mid] < rand:
                left = mid + 1
            else:
                return mid
        return res
        # for i in range(len(self.w)):
        #     rand -= self.w[i]
        #     if rand < 0:
        #         break
        # return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
testcases = [
    ["Solution", "pickIndex"],
    [[[1, 3, 5]], []],
    [
        "Solution",
        "pickIndex",
        "pickIndex",
        "pickIndex",
        "pickIndex",
        "pickIndex",
        "pickIndex",
        "pickIndex",
        "pickIndex",
        "pickIndex",
    ],
    [[[1, 3, 5]], [], [], [], [], [], [], [], [], []],
]

for i in range(0, len(testcases), 2):
    obj = globals()[testcases[i][0]](*testcases[i + 1][0])
    print(None)
    for j in range(1, len(testcases[i])):
        method = getattr(obj, testcases[i][j])
        print(method(*testcases[i + 1][j]))
