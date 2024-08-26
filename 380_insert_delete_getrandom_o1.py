# [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
import random


class RandomizedSet:
    def __init__(self):
        self.store = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        self.lst.append(val)
        self.store[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False

        idx = self.store[val]
        self.lst[idx], self.lst[-1] = self.lst[-1], self.lst[idx]
        self.lst.pop()

        if idx < len(self.lst):
            self.store[self.lst[idx]] = idx
        del self.store[val]
        return True

    def getRandom(self) -> int:
        return self.lst[random.randrange(len(self.lst))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
testcases = [
    [
        "RandomizedSet",
        "insert",
        "remove",
        "insert",
        "getRandom",
        "remove",
        "insert",
        "getRandom",
    ],
    [[], [1], [2], [2], [], [1], [2], []],
    ["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"],
    [[], [0], [0], [0], [], [0], [0]],
]

for i in range(0, len(testcases), 2):
    obj = globals()[testcases[i][0]](*testcases[i + 1][0])
    print(None)
    for j in range(1, len(testcases[i])):
        method = getattr(obj, testcases[i][j])
        print(method(*testcases[i + 1][j]))
